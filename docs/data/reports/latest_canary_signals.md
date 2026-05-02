# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T16:45:21.520959+00:00`
- Correlation status: `ready`
- Asset price records: `90`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `7`; crypto_alt avg `0.0507` n `223`; crypto_major avg `0.0167` n `7`; equity avg `0.0136` n `42`; fx avg `0.0051` n `4`; index avg `-0.0024` n `9`; metal avg `0.0033` n `7`; unknown avg `0.0765` n `313`
- 1h: commodity avg `-0.0117` n `7`; crypto_alt avg `0.1776` n `223`; crypto_major avg `0.0473` n `7`; equity avg `0.0485` n `42`; fx avg `0.0053` n `4`; index avg `0.0027` n `9`; metal avg `0.0069` n `7`; unknown avg `0.0839` n `313`
- 4h: commodity avg `-0.0244` n `7`; crypto_alt avg `1.12` n `223`; crypto_major avg `0.3597` n `7`; equity avg `0.0819` n `42`; fx avg `0.0469` n `4`; index avg `-0.0037` n `9`; metal avg `-0.0175` n `7`; unknown avg `0.0516` n `313`
- 24h: commodity avg `0.6219` n `7`; crypto_alt avg `1.211` n `223`; crypto_major avg `0.1268` n `7`; equity avg `0.3454` n `42`; fx avg `-0.0816` n `4`; index avg `0.1837` n `9`; metal avg `-0.6607` n `7`; unknown avg `0.6184` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5277`, n `86`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5232`, n `82`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5093`, n `86`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4954`, n `82`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4753`, n `82`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4746`, n `82`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4613`, n `82`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.452`, n `86`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4276`, n `82`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4268`, n `86`, moderate_sample_signal
