# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T13:07:28.922211+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1637` n `12`; crypto_alt avg `-0.34` n `229`; crypto_major avg `-0.3885` n `8`; equity avg `-0.1364` n `91`; fx avg `-0.0093` n `6`; index avg `-0.0376` n `25`; metal avg `-0.1134` n `20`; unknown avg `-0.1089` n `764`
- 1h: commodity avg `0.009` n `12`; crypto_alt avg `-0.7028` n `229`; crypto_major avg `-0.7752` n `8`; equity avg `-0.0374` n `91`; fx avg `-0.013` n `6`; index avg `0.0174` n `25`; metal avg `-0.0145` n `20`; unknown avg `-0.0903` n `757`
- 4h: commodity avg `-0.2427` n `12`; crypto_alt avg `0.094` n `229`; crypto_major avg `-0.0001` n `8`; equity avg `1.0771` n `91`; fx avg `-0.0441` n `6`; index avg `0.2668` n `25`; metal avg `0.0982` n `20`; unknown avg `-0.0093` n `757`
- 24h: commodity avg `1.4113` n `12`; crypto_alt avg `-3.8252` n `229`; crypto_major avg `-3.3298` n `8`; equity avg `-2.1741` n `91`; fx avg `-0.1022` n `6`; index avg `-0.4978` n `25`; metal avg `-1.321` n `20`; unknown avg `-0.4784` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
