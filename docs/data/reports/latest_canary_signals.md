# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T22:15:30.338893+00:00`
- Correlation status: `ready`
- Asset price records: `112`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `7`; crypto_alt avg `-0.0131` n `223`; crypto_major avg `-0.0746` n `7`; equity avg `-0.0314` n `42`; fx avg `-0.0032` n `4`; index avg `-0.0052` n `9`; metal avg `0.0055` n `7`; unknown avg `0.0987` n `313`
- 1h: commodity avg `-0.0247` n `7`; crypto_alt avg `0.1488` n `223`; crypto_major avg `0.2186` n `7`; equity avg `0.0208` n `42`; fx avg `0.0226` n `4`; index avg `-0.0253` n `9`; metal avg `0.0101` n `7`; unknown avg `0.0954` n `313`
- 4h: commodity avg `-0.0379` n `7`; crypto_alt avg `0.8506` n `223`; crypto_major avg `0.3866` n `7`; equity avg `0.3755` n `42`; fx avg `0.0409` n `4`; index avg `0.0145` n `9`; metal avg `0.0011` n `7`; unknown avg `0.4208` n `313`
- 24h: commodity avg `-0.1797` n `7`; crypto_alt avg `1.8189` n `223`; crypto_major avg `0.4266` n `7`; equity avg `0.8509` n `42`; fx avg `0.0465` n `4`; index avg `-0.0516` n `9`; metal avg `0.0239` n `7`; unknown avg `0.4466` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5304`, n `104`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5118`, n `104`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.488`, n `108`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.471`, n `108`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4535`, n `104`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4212`, n `104`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.418`, n `104`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4177`, n `104`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4163`, n `104`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4082`, n `108`, moderate_sample_signal
