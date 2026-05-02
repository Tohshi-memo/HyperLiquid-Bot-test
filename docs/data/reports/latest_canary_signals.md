# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T21:30:21.942973+00:00`
- Correlation status: `ready`
- Asset price records: `109`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `7`; crypto_alt avg `0.1247` n `223`; crypto_major avg `0.0301` n `7`; equity avg `0.0144` n `42`; fx avg `0.0226` n `4`; index avg `-0.0216` n `9`; metal avg `-0.0059` n `7`; unknown avg `0.0153` n `313`
- 1h: commodity avg `0.0593` n `7`; crypto_alt avg `0.1668` n `223`; crypto_major avg `0.0304` n `7`; equity avg `0.1735` n `42`; fx avg `0.0268` n `4`; index avg `-0.006` n `9`; metal avg `-0.0052` n `7`; unknown avg `0.0067` n `313`
- 4h: commodity avg `-0.1018` n `7`; crypto_alt avg `0.4677` n `223`; crypto_major avg `0.0094` n `7`; equity avg `0.4887` n `42`; fx avg `0.042` n `4`; index avg `0.035` n `9`; metal avg `-0.0539` n `7`; unknown avg `0.1976` n `313`
- 24h: commodity avg `0.0008` n `7`; crypto_alt avg `1.8207` n `223`; crypto_major avg `0.2363` n `7`; equity avg `1.1335` n `42`; fx avg `0.0154` n `4`; index avg `0.055` n `9`; metal avg `-0.1022` n `7`; unknown avg `0.3676` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5408`, n `101`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5389`, n `101`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5068`, n `105`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4893`, n `105`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4685`, n `101`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4212`, n `101`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4196`, n `101`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4182`, n `101`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4178`, n `101`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4131`, n `105`, moderate_sample_signal
