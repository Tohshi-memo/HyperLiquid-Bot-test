# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T16:15:20.155279+00:00`
- Correlation status: `ready`
- Asset price records: `88`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `7`; crypto_alt avg `0.1266` n `223`; crypto_major avg `0.0875` n `7`; equity avg `0.038` n `42`; fx avg `-0.008` n `4`; index avg `-0.0039` n `9`; metal avg `0.0068` n `7`; unknown avg `-0.1459` n `313`
- 1h: commodity avg `-0.0067` n `7`; crypto_alt avg `0.3354` n `223`; crypto_major avg `0.1757` n `7`; equity avg `0.0896` n `42`; fx avg `0.0032` n `4`; index avg `0.0102` n `9`; metal avg `-0.0011` n `7`; unknown avg `-0.0238` n `313`
- 4h: commodity avg `-0.0142` n `7`; crypto_alt avg `1.4126` n `223`; crypto_major avg `0.5589` n `7`; equity avg `0.0868` n `42`; fx avg `0.028` n `4`; index avg `0.0299` n `9`; metal avg `-0.0146` n `7`; unknown avg `0.045` n `313`
- 24h: commodity avg `0.6297` n `7`; crypto_alt avg `1.2664` n `223`; crypto_major avg `0.2224` n `7`; equity avg `0.3616` n `42`; fx avg `-0.0949` n `4`; index avg `0.1872` n `9`; metal avg `-0.664` n `7`; unknown avg `0.5451` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5267`, n `84`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5231`, n `80`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5083`, n `84`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5021`, n `80`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4765`, n `80`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4743`, n `80`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.461`, n `80`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.453`, n `84`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4318`, n `84`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4273`, n `80`, moderate_sample_signal
