# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T23:30:27.532272+00:00`
- Correlation status: `ready`
- Asset price records: `213`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1289` n `7`; crypto_alt avg `-0.3909` n `223`; crypto_major avg `-0.5461` n `7`; equity avg `-0.1345` n `42`; fx avg `0.0035` n `4`; index avg `0.0874` n `9`; metal avg `0.0318` n `7`; unknown avg `0.277` n `314`
- 1h: commodity avg `0.2951` n `7`; crypto_alt avg `-0.5876` n `223`; crypto_major avg `-0.5284` n `7`; equity avg `-0.3255` n `42`; fx avg `-0.0067` n `4`; index avg `0.0988` n `9`; metal avg `0.0569` n `7`; unknown avg `0.0305` n `314`
- 4h: commodity avg `0.1456` n `7`; crypto_alt avg `-0.3582` n `223`; crypto_major avg `-0.1954` n `7`; equity avg `-0.2196` n `42`; fx avg `-0.0523` n `4`; index avg `0.0443` n `9`; metal avg `-0.0314` n `7`; unknown avg `0.036` n `314`
- 24h: commodity avg `0.005` n `7`; crypto_alt avg `-0.6207` n `223`; crypto_major avg `-0.1796` n `7`; equity avg `-0.0529` n `42`; fx avg `-0.023` n `4`; index avg `0.128` n `9`; metal avg `0.4242` n `7`; unknown avg `0.2655` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3915`, n `209`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3742`, n `209`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.314`, n `209`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3035`, n `209`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2998`, n `205`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.299`, n `205`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2864`, n `209`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.278`, n `209`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2679`, n `209`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2523`, n `205`, moderate_sample_signal
