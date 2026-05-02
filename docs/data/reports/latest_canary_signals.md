# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T10:15:23.732023+00:00`
- Correlation status: `ready`
- Asset price records: `64`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `7`; crypto_alt avg `0.0023` n `223`; crypto_major avg `0.0139` n `7`; equity avg `0.0034` n `42`; fx avg `0.0061` n `4`; index avg `-0.0316` n `9`; metal avg `0.003` n `7`; unknown avg `-0.0567` n `313`
- 1h: commodity avg `-0.0101` n `7`; crypto_alt avg `0.0127` n `223`; crypto_major avg `-0.0986` n `7`; equity avg `-0.001` n `42`; fx avg `-0.0072` n `4`; index avg `-0.04` n `9`; metal avg `0.0156` n `7`; unknown avg `-0.1026` n `313`
- 4h: commodity avg `0.0234` n `7`; crypto_alt avg `0.5021` n `223`; crypto_major avg `0.3212` n `7`; equity avg `0.0297` n `42`; fx avg `0.0208` n `4`; index avg `-0.068` n `9`; metal avg `0.0811` n `7`; unknown avg `0.1733` n `311`
- 24h: crypto_alt avg `0.8983` n `223`; crypto_major avg `0.7697` n `7`; metal avg `0.7884` n `1`; unknown avg `1.4118` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5769`, n `60`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5697`, n `56`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5662`, n `56`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5568`, n `60`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4939`, n `56`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4818`, n `56`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4753`, n `60`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4686`, n `56`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4424`, n `60`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4416`, n `60`, moderate_sample_signal
