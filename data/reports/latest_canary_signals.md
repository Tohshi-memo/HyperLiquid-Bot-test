# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T03:45:20.815737+00:00`
- Correlation status: `ready`
- Asset price records: `230`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8871` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0971` n `7`; crypto_alt avg `-0.0616` n `223`; crypto_major avg `-0.1051` n `7`; equity avg `-0.0272` n `42`; fx avg `-0.0779` n `4`; index avg `-0.0194` n `9`; metal avg `-0.0092` n `7`; unknown avg `-0.0097` n `314`
- 1h: commodity avg `0.0922` n `7`; crypto_alt avg `-0.0503` n `223`; crypto_major avg `-0.17` n `7`; equity avg `0.0489` n `42`; fx avg `-0.071` n `4`; index avg `0.074` n `9`; metal avg `0.1065` n `7`; unknown avg `0.0173` n `314`
- 4h: commodity avg `0.1352` n `7`; crypto_alt avg `1.7368` n `223`; crypto_major avg `1.9146` n `7`; equity avg `1.2589` n `42`; fx avg `-0.025` n `4`; index avg `0.8085` n `9`; metal avg `0.0275` n `7`; unknown avg `0.1132` n `314`
- 24h: commodity avg `0.1558` n `7`; crypto_alt avg `2.4594` n `223`; crypto_major avg `2.5141` n `7`; equity avg `1.2195` n `42`; fx avg `-0.0557` n `4`; index avg `0.7592` n `9`; metal avg `0.3441` n `7`; unknown avg `0.5039` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3962`, n `222`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3859`, n `222`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.366`, n `226`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3504`, n `226`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.216`, n `222`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1994`, n `222`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1933`, n `226`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1886`, n `226`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1829`, n `226`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1407`, n `226`, weak_sample_signal
