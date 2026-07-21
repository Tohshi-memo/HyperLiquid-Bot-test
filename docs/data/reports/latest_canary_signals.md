# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T22:41:03.089295+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0225` n `12`; crypto_alt avg `-0.0863` n `230`; crypto_major avg `0.0328` n `8`; equity avg `-0.069` n `98`; fx avg `0.0` n `6`; index avg `-0.0057` n `25`; metal avg `0.0227` n `20`; unknown avg `-0.0299` n `771`
- 1h: commodity avg `0.0318` n `12`; crypto_alt avg `-0.2133` n `230`; crypto_major avg `-0.0943` n `8`; equity avg `-0.1867` n `98`; fx avg `0.009` n `6`; index avg `-0.0232` n `25`; metal avg `0.0104` n `20`; unknown avg `-0.1715` n `771`
- 4h: commodity avg `0.1275` n `12`; crypto_alt avg `-0.1196` n `230`; crypto_major avg `-0.1012` n `8`; equity avg `0.5193` n `98`; fx avg `-0.0004` n `6`; index avg `0.0105` n `25`; metal avg `-0.0112` n `20`; unknown avg `-0.2316` n `771`
- 24h: commodity avg `0.4854` n `12`; crypto_alt avg `0.8945` n `230`; crypto_major avg `0.8349` n `8`; equity avg `4.3782` n `98`; fx avg `0.0673` n `6`; index avg `0.6844` n `25`; metal avg `0.8055` n `20`; unknown avg `0.1637` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0913`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0524`, n `666`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
