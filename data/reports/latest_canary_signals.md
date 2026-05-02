# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T14:30:20.809844+00:00`
- Correlation status: `ready`
- Asset price records: `81`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `7`; crypto_alt avg `0.211` n `223`; crypto_major avg `0.1223` n `7`; equity avg `-0.0179` n `42`; fx avg `-0.0005` n `4`; index avg `-0.0019` n `9`; metal avg `0.0017` n `7`; unknown avg `0.272` n `313`
- 1h: commodity avg `0.0053` n `7`; crypto_alt avg `0.6106` n `223`; crypto_major avg `0.1108` n `7`; equity avg `-0.0201` n `42`; fx avg `0.0056` n `4`; index avg `-0.0093` n `9`; metal avg `-0.0186` n `7`; unknown avg `0.171` n `313`
- 4h: commodity avg `-0.0329` n `7`; crypto_alt avg `0.803` n `223`; crypto_major avg `0.22` n `7`; equity avg `-0.0067` n `42`; fx avg `-0.0176` n `4`; index avg `0.0469` n `9`; metal avg `-0.0106` n `7`; unknown avg `0.1236` n `313`
- 24h: commodity avg `0.6204` n `7`; crypto_alt avg `0.8903` n `223`; crypto_major avg `0.138` n `7`; equity avg `0.8073` n `42`; fx avg `-0.1417` n `4`; index avg `0.0268` n `9`; metal avg `-0.7298` n `7`; unknown avg `1.4203` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5369`, n `77`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5182`, n `77`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5154`, n `73`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5055`, n `73`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4767`, n `73`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.465`, n `73`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4648`, n `73`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4626`, n `77`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4418`, n `77`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4246`, n `73`, moderate_sample_signal
