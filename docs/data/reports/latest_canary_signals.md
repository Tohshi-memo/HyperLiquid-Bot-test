# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T03:00:29.611204+00:00`
- Correlation status: `ready`
- Asset price records: `35`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `7`; crypto_alt avg `-0.1048` n `223`; crypto_major avg `0.016` n `7`; equity avg `-0.0138` n `42`; fx avg `0.0024` n `4`; index avg `-0.001` n `9`; metal avg `0.0109` n `7`; unknown avg `-0.0014` n `311`
- 1h: commodity avg `0.0204` n `7`; crypto_alt avg `-0.2481` n `223`; crypto_major avg `0.0427` n `7`; equity avg `0.0587` n `42`; fx avg `-0.017` n `4`; index avg `0.0163` n `9`; metal avg `0.0055` n `7`; unknown avg `-0.0423` n `311`
- 4h: commodity avg `0.018` n `7`; crypto_alt avg `0.0121` n `223`; crypto_major avg `0.3617` n `7`; equity avg `0.1517` n `42`; fx avg `0.0119` n `4`; index avg `-0.071` n `9`; metal avg `0.004` n `7`; unknown avg `-0.0228` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6671`, n `31`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6432`, n `31`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5413`, n `31`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5321`, n `27`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5123`, n `27`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5066`, n `31`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5052`, n `31`, strong_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4859`, n `31`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.4801`, n `31`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4667`, n `27`, moderate_sample_signal
