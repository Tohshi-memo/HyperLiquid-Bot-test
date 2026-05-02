# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T15:15:35.150154+00:00`
- Correlation status: `ready`
- Asset price records: `84`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `7`; crypto_alt avg `0.0697` n `223`; crypto_major avg `0.0317` n `7`; equity avg `0.0274` n `42`; fx avg `0.0032` n `4`; index avg `-0.0015` n `9`; metal avg `0.0095` n `7`; unknown avg `-0.0162` n `313`
- 1h: commodity avg `-0.0195` n `7`; crypto_alt avg `0.4251` n `223`; crypto_major avg `0.1449` n `7`; equity avg `-0.0381` n `42`; fx avg `0.0386` n `4`; index avg `-0.0083` n `9`; metal avg `0.0014` n `7`; unknown avg `0.1412` n `313`
- 4h: commodity avg `-0.0824` n `7`; crypto_alt avg `1.1641` n `223`; crypto_major avg `0.2971` n `7`; equity avg `0.0103` n `42`; fx avg `0.0354` n `4`; index avg `0.0337` n `9`; metal avg `-0.0097` n `7`; unknown avg `-0.062` n `313`
- 24h: commodity avg `0.2802` n `7`; crypto_alt avg `1.1395` n `223`; crypto_major avg `-0.1176` n `7`; equity avg `0.5567` n `42`; fx avg `-0.1128` n `4`; index avg `0.0705` n `9`; metal avg `-0.3302` n `7`; unknown avg `0.8707` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5396`, n `76`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.536`, n `76`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5351`, n `80`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5165`, n `80`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4784`, n `76`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4781`, n `76`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4654`, n `76`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4472`, n `80`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4353`, n `80`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4254`, n `76`, moderate_sample_signal
