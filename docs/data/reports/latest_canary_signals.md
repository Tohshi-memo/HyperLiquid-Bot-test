# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T11:07:26.807723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0734` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0626` n `13`; crypto_alt avg `-0.0488` n `239`; crypto_major avg `-0.0379` n `8`; equity avg `-0.1061` n `160`; fx avg `0.004` n `6`; index avg `0.0089` n `27`; metal avg `-0.0334` n `20`; unknown avg `19.0232` n `1258`
- 1h: commodity avg `0.277` n `13`; crypto_alt avg `-0.1936` n `239`; crypto_major avg `-0.4025` n `8`; equity avg `-0.7654` n `160`; fx avg `0.0132` n `6`; index avg `-0.0406` n `27`; metal avg `-0.0918` n `20`; unknown avg `19.8141` n `1256`
- 4h: commodity avg `-0.0547` n `13`; crypto_alt avg `-0.6531` n `239`; crypto_major avg `-1.1055` n `8`; equity avg `-0.3651` n `160`; fx avg `-0.0039` n `6`; index avg `-0.0321` n `27`; metal avg `-0.2597` n `20`; unknown avg `19.4049` n `1219`
- 24h: commodity avg `-0.4965` n `13`; crypto_alt avg `0.8558` n `239`; crypto_major avg `0.1402` n `8`; equity avg `3.7748` n `160`; fx avg `-0.04` n `6`; index avg `0.4285` n `27`; metal avg `-0.0379` n `20`; unknown avg `5.6458` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2329`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
