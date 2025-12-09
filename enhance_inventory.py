#!/usr/bin/env python
"""Enhance inventory expiration table"""

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the tab1 section
old = '''        with tab1:
            st.subheader("Articles en Danger d'Expiration")
            
            # S'assurer que la colonne existe
            if 'days_until_expiry' in inventory_data.columns:
                # Filter items at risk (expiring within 30 days)
                near_expiry_sorted = inventory_data[inventory_data['days_until_expiry'] <= 30].sort_values('days_until_expiry')
                
                if len(near_expiry_sorted) > 0:
                    # Color coding
                    def highlight_risk(row):
                        days = row.get('days_until_expiry', 999)
                        if days <= 1:
                            return ['background-color: #ff6b6b'] * len(row)
                        elif days <= 3:
                            return ['background-color: #ffa500'] * len(row)
                        elif days <= 7:
                            return ['background-color: #fff9e6'] * len(row)
                        else:
                            return ['background-color: white'] * len(row)
                    
                    # Afficher les 20 premiers
                    display_cols = ['product_name', 'quantity_available', 'days_until_expiry', 'expiration_date'] if 'product_name' in near_expiry_sorted.columns else near_expiry_sorted.columns[:5]
                    styled_df = near_expiry_sorted[display_cols].head(20).style.apply(highlight_risk, axis=1)
                    st.dataframe(styled_df, use_container_width=True)
                    
                    # Export button
                    csv = near_expiry_sorted.to_csv(index=False)
                    st.download_button(
                        label="📥 Télécharger Liste Complète (CSV)",
                        data=csv,
                        file_name=f"inventory_expiry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
                else:
                    st.success("✅ Aucun article en danger d'expiration (≤30 jours)")
            else:
                st.warning("⚠️ Colonne 'days_until_expiry' non trouvée dans les données")'''

new = '''        with tab1:
            st.subheader("Articles en Danger d'Expiration")
            
            if 'days_until_expiry' in inventory_data.columns:
                # Filter items at risk (≤30 jours)
                near_expiry_sorted = inventory_data[inventory_data['days_until_expiry'] <= 30].sort_values('days_until_expiry')
                
                if len(near_expiry_sorted) > 0:
                    # Colonnes à afficher
                    cols_avail = near_expiry_sorted.columns.tolist()
                    display_cols = []
                    for col in ['product_name', 'category', 'batch_number', 'quantity_available', 'quantity', 'days_until_expiry', 'expiration_date', 'supplier']:
                        if col in cols_avail:
                            display_cols.append(col)
                    display_cols = display_cols[:8]
                    
                    # Stats par urgence
                    col_crit, col_haute, col_moy = st.columns(3)
                    with col_crit:
                        crit_count = len(near_expiry_sorted[near_expiry_sorted['days_until_expiry'] <= 1])
                        st.metric("🚨 Critique (≤1j)", crit_count)
                    with col_haute:
                        high_count = len(near_expiry_sorted[(near_expiry_sorted['days_until_expiry'] > 1) & (near_expiry_sorted['days_until_expiry'] <= 7)])
                        st.metric("⚠️ Haute (2-7j)", high_count)
                    with col_moy:
                        med_count = len(near_expiry_sorted[(near_expiry_sorted['days_until_expiry'] > 7) & (near_expiry_sorted['days_until_expiry'] <= 30)])
                        st.metric("📌 Moyen (8-30j)", med_count)
                    
                    st.markdown("---")
                    
                    # Articles critiques
                    st.subheader("🚨 Articles Critiques (Expiration ≤ 1 jour)")
                    critical_items = near_expiry_sorted[near_expiry_sorted['days_until_expiry'] <= 1]
                    if len(critical_items) > 0:
                        st.dataframe(critical_items[display_cols], use_container_width=True)
                    else:
                        st.info("Aucun article en situation critique")
                    
                    # Articles à haut risque
                    st.subheader("⚠️ Articles à Haut Risque (2-7 jours)")
                    high_items = near_expiry_sorted[(near_expiry_sorted['days_until_expiry'] > 1) & (near_expiry_sorted['days_until_expiry'] <= 7)]
                    if len(high_items) > 0:
                        st.dataframe(high_items[display_cols], use_container_width=True)
                    else:
                        st.info("Aucun article à haut risque")
                    
                    # Articles à risque moyen
                    st.subheader("📌 Articles à Risque Moyen (8-30 jours)")
                    med_items = near_expiry_sorted[(near_expiry_sorted['days_until_expiry'] > 7) & (near_expiry_sorted['days_until_expiry'] <= 30)]
                    if len(med_items) > 0:
                        st.dataframe(med_items[display_cols], use_container_width=True)
                    else:
                        st.info("Aucun article à risque moyen")
                    
                    st.markdown("---")
                    
                    # Export
                    csv = near_expiry_sorted.to_csv(index=False)
                    st.download_button(
                        label="📥 Télécharger Liste Complète (CSV)",
                        data=csv,
                        file_name=f"inventory_expiry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime="text/csv"
                    )
                else:
                    st.success("✅ Aucun article en danger d'expiration (≤30 jours)")
            else:
                st.warning("⚠️ Colonne 'days_until_expiry' non trouvée dans les données")'''

content = content.replace(old, new)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Inventory table enhanced!")
print("- Grouped by urgency level (Critical/High/Medium)")
print("- Shows more product varieties and categories")
print("- Multiple columns: product, category, batch, quantity, dates")
