# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T13:52:33.483717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1008` n `12`; crypto_alt avg `0.1472` n `229`; crypto_major avg `0.2586` n `8`; equity avg `-0.3465` n `91`; fx avg `-0.0088` n `6`; index avg `-0.0239` n `25`; metal avg `-0.0395` n `20`; unknown avg `0.1453` n `763`
- 1h: commodity avg `0.304` n `12`; crypto_alt avg `-0.3434` n `229`; crypto_major avg `-0.3463` n `8`; equity avg `-0.7339` n `91`; fx avg `-0.0038` n `6`; index avg `-0.0692` n `25`; metal avg `0.0252` n `20`; unknown avg `0.0369` n `763`
- 4h: commodity avg `0.0845` n `12`; crypto_alt avg `-0.0509` n `229`; crypto_major avg `-0.0765` n `8`; equity avg `-0.7919` n `91`; fx avg `-0.0546` n `6`; index avg `-0.0782` n `25`; metal avg `0.3232` n `20`; unknown avg `-0.0221` n `763`
- 24h: commodity avg `0.3715` n `12`; crypto_alt avg `0.8992` n `229`; crypto_major avg `0.9282` n `8`; equity avg `-2.5397` n `90`; fx avg `-0.1717` n `6`; index avg `-0.5001` n `25`; metal avg `0.1229` n `20`; unknown avg `0.2501` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
