# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T11:15:35.091775+00:00`
- Correlation status: `ready`
- Asset price records: `68`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0025` n `7`; crypto_alt avg `0.021` n `223`; crypto_major avg `0.0175` n `7`; equity avg `-0.0058` n `42`; fx avg `-0.0104` n `4`; index avg `0.0001` n `9`; metal avg `-0.0013` n `7`; unknown avg `0.025` n `313`
- 1h: commodity avg `0.0297` n `7`; crypto_alt avg `-0.1628` n `223`; crypto_major avg `-0.1575` n `7`; equity avg `0.03` n `42`; fx avg `-0.0138` n `4`; index avg `0.042` n `9`; metal avg `0.0002` n `7`; unknown avg `0.055` n `313`
- 4h: commodity avg `0.0848` n `7`; crypto_alt avg `0.1827` n `223`; crypto_major avg `0.0109` n `7`; equity avg `-0.0591` n `42`; fx avg `0.0056` n `4`; index avg `-0.0117` n `9`; metal avg `0.0516` n `7`; unknown avg `0.2606` n `311`
- 24h: crypto_alt avg `0.729` n `223`; crypto_major avg `0.6104` n `7`; metal avg `0.7862` n `1`; unknown avg `1.4362` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5749`, n `64`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.555`, n `64`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5545`, n `60`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.543`, n `60`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4795`, n `64`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4741`, n `60`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4708`, n `60`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4605`, n `60`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4445`, n `64`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4365`, n `64`, moderate_sample_signal
