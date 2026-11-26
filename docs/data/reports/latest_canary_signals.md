# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T15:22:41.258731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1217` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0014` n `13`; crypto_alt avg `0.405` n `239`; crypto_major avg `0.3325` n `8`; equity avg `0.1375` n `168`; fx avg `-0.0042` n `6`; index avg `0.0056` n `27`; metal avg `-0.0423` n `20`; unknown avg `0.0652` n `1265`
- 1h: commodity avg `-0.0157` n `13`; crypto_alt avg `-0.9373` n `239`; crypto_major avg `-1.113` n `8`; equity avg `-0.1143` n `168`; fx avg `-0.0228` n `6`; index avg `0.0087` n `27`; metal avg `0.0189` n `20`; unknown avg `-0.2429` n `1263`
- 4h: commodity avg `0.0683` n `13`; crypto_alt avg `-0.8949` n `239`; crypto_major avg `-0.8909` n `8`; equity avg `-0.0514` n `168`; fx avg `0.0079` n `6`; index avg `-0.0091` n `27`; metal avg `-0.0056` n `20`; unknown avg `160.2914` n `1253`
- 24h: commodity avg `0.2781` n `13`; crypto_alt avg `4.8207` n `239`; crypto_major avg `3.9015` n `8`; equity avg `6.3692` n `168`; fx avg `0.0614` n `6`; index avg `0.5813` n `27`; metal avg `1.5221` n `20`; unknown avg `207.3611` n `1062`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
