# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T18:32:53.862180+00:00`
- Correlation status: `ready`
- Asset price records: `97`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0049` n `7`; crypto_alt avg `0.3867` n `223`; crypto_major avg `0.2119` n `7`; equity avg `0.039` n `42`; fx avg `0.0` n `4`; index avg `0.0036` n `9`; metal avg `-0.0027` n `7`; unknown avg `0.0823` n `313`
- 1h: commodity avg `-0.0945` n `7`; crypto_alt avg `0.0289` n `223`; crypto_major avg `0.0233` n `7`; equity avg `0.1561` n `42`; fx avg `0.0011` n `4`; index avg `0.0205` n `9`; metal avg `-0.0418` n `7`; unknown avg `0.0192` n `313`
- 4h: commodity avg `-0.1701` n `7`; crypto_alt avg `0.7236` n `223`; crypto_major avg `0.1611` n `7`; equity avg `0.2408` n `42`; fx avg `0.0823` n `4`; index avg `0.0315` n `9`; metal avg `-0.0288` n `7`; unknown avg `-0.0451` n `313`
- 24h: commodity avg `0.0334` n `7`; crypto_alt avg `1.2903` n `223`; crypto_major avg `0.1927` n `7`; equity avg `0.7567` n `42`; fx avg `-0.0287` n `4`; index avg `0.0832` n `9`; metal avg `-0.2783` n `7`; unknown avg `0.4071` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5363`, n `89`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5237`, n `93`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5125`, n `89`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5055`, n `93`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4763`, n `89`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4348`, n `89`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4292`, n `93`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4256`, n `89`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4242`, n `89`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4221`, n `89`, moderate_sample_signal
