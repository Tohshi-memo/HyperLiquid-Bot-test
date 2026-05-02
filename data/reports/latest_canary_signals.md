# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T16:00:29.302911+00:00`
- Correlation status: `ready`
- Asset price records: `87`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0075` n `7`; crypto_alt avg `0.0967` n `223`; crypto_major avg `0.0553` n `7`; equity avg `0.0281` n `42`; fx avg `0.0` n `4`; index avg `0.0102` n `9`; metal avg `-0.0033` n `7`; unknown avg `0.2049` n `313`
- 1h: commodity avg `-0.0148` n `7`; crypto_alt avg `0.2781` n `223`; crypto_major avg `0.1198` n `7`; equity avg `0.0787` n `42`; fx avg `0.0144` n `4`; index avg `0.0126` n `9`; metal avg `0.0016` n `7`; unknown avg `0.1631` n `313`
- 4h: commodity avg `-0.0214` n `7`; crypto_alt avg `1.3397` n `223`; crypto_major avg `0.453` n `7`; equity avg `0.0187` n `42`; fx avg `0.0346` n `4`; index avg `0.0339` n `9`; metal avg `-0.0154` n `7`; unknown avg `0.248` n `313`
- 24h: commodity avg `0.27` n `7`; crypto_alt avg `1.3302` n `223`; crypto_major avg `-0.0293` n `7`; equity avg `0.6155` n `42`; fx avg `-0.1017` n `4`; index avg `0.0846` n `9`; metal avg `-0.3381` n `7`; unknown avg `1.0501` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5314`, n `79`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5305`, n `83`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5148`, n `79`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.512`, n `83`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4775`, n `79`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4765`, n `79`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4634`, n `79`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4507`, n `83`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4315`, n `83`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4269`, n `79`, moderate_sample_signal
