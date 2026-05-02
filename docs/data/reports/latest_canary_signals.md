# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T13:45:18.631687+00:00`
- Correlation status: `ready`
- Asset price records: `78`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `7`; crypto_alt avg `0.1341` n `223`; crypto_major avg `0.0898` n `7`; equity avg `0.0468` n `42`; fx avg `-0.0019` n `4`; index avg `-0.004` n `9`; metal avg `-0.0256` n `7`; unknown avg `0.0324` n `313`
- 1h: commodity avg `-0.0006` n `7`; crypto_alt avg `0.1347` n `223`; crypto_major avg `0.2363` n `7`; equity avg `0.0948` n `42`; fx avg `-0.0163` n `4`; index avg `0.0015` n `9`; metal avg `-0.0265` n `7`; unknown avg `-0.0082` n `313`
- 4h: commodity avg `-0.0492` n `7`; crypto_alt avg `0.2197` n `223`; crypto_major avg `0.0163` n `7`; equity avg `0.1262` n `42`; fx avg `-0.0173` n `4`; index avg `0.0484` n `9`; metal avg `-0.0087` n `7`; unknown avg `-0.0683` n `313`
- 24h: commodity avg `0.5024` n `7`; crypto_alt avg `0.161` n `223`; crypto_major avg `-0.3289` n `7`; equity avg `0.8476` n `42`; fx avg `-0.126` n `4`; index avg `0.1521` n `9`; metal avg `-0.659` n `7`; unknown avg `0.9075` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5473`, n `74`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5312`, n `70`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5311`, n `70`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5284`, n `74`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4965`, n `74`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4765`, n `70`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4717`, n `70`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4649`, n `70`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4593`, n `74`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.459`, n `74`, moderate_sample_signal
