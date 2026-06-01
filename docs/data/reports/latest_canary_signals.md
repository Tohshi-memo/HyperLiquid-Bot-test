# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T01:52:16.464720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0333` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.1616` n `228`; crypto_major avg `-0.3569` n `8`; equity avg `0.0602` n `69`; fx avg `0.0008` n `6`; index avg `0.0032` n `23`; metal avg `0.1022` n `18`; unknown avg `-0.0681` n `421`
- 1h: commodity avg `0.2442` n `12`; crypto_alt avg `-0.8568` n `228`; crypto_major avg `-1.1223` n `8`; equity avg `-0.0935` n `69`; fx avg `0.0284` n `6`; index avg `-0.089` n `23`; metal avg `-0.0163` n `18`; unknown avg `-0.3959` n `421`
- 4h: commodity avg `0.7036` n `12`; crypto_alt avg `0.2715` n `228`; crypto_major avg `-0.4028` n `8`; equity avg `-0.0663` n `69`; fx avg `0.0798` n `6`; index avg `-0.0117` n `23`; metal avg `0.3546` n `18`; unknown avg `0.4169` n `421`
- 24h: commodity avg `1.0437` n `12`; crypto_alt avg `0.461` n `228`; crypto_major avg `-0.6305` n `8`; equity avg `0.5067` n `69`; fx avg `0.0445` n `6`; index avg `0.3291` n `23`; metal avg `0.2552` n `18`; unknown avg `1.3287` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2836`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2559`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
