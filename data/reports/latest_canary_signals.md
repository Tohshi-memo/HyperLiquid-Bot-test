# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T00:37:37.897968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3479` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7889` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7309` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.5887` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `-0.2696` n `230`; crypto_major avg `-0.2328` n `8`; equity avg `-0.0083` n `92`; fx avg `0.0031` n `6`; index avg `-0.0116` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.1206` n `765`
- 1h: commodity avg `0.2106` n `12`; crypto_alt avg `-0.4473` n `230`; crypto_major avg `-0.5558` n `8`; equity avg `0.0014` n `92`; fx avg `-0.0064` n `6`; index avg `-0.0063` n `25`; metal avg `-0.0244` n `20`; unknown avg `-0.2973` n `765`
- 4h: commodity avg `0.5087` n `12`; crypto_alt avg `-2.1587` n `230`; crypto_major avg `-1.8392` n `8`; equity avg `-0.2505` n `92`; fx avg `0.0193` n `6`; index avg `-0.1083` n `25`; metal avg `-0.0503` n `20`; unknown avg `1.2695` n `765`
- 24h: commodity avg `0.5132` n `12`; crypto_alt avg `-1.0618` n `229`; crypto_major avg `-0.9161` n `8`; equity avg `0.0658` n `92`; fx avg `0.0262` n `6`; index avg `-0.074` n `25`; metal avg `-0.0668` n `20`; unknown avg `0.1193` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
