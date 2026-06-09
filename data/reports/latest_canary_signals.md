# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T19:29:29.751676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `-0.0648` n `228`; crypto_major avg `-0.0506` n `8`; equity avg `-0.3233` n `74`; fx avg `0.0075` n `6`; index avg `-0.244` n `23`; metal avg `-0.2893` n `18`; unknown avg `-0.0455` n `547`
- 1h: commodity avg `0.0135` n `12`; crypto_alt avg `-0.0508` n `228`; crypto_major avg `-0.1462` n `8`; equity avg `0.1021` n `74`; fx avg `-0.0112` n `6`; index avg `0.2116` n `23`; metal avg `-0.2287` n `18`; unknown avg `-0.0621` n `547`
- 4h: commodity avg `0.0567` n `12`; crypto_alt avg `0.5029` n `228`; crypto_major avg `0.1701` n `8`; equity avg `-0.4552` n `74`; fx avg `-0.0437` n `6`; index avg `-0.6958` n `23`; metal avg `-0.6369` n `18`; unknown avg `-0.2345` n `547`
- 24h: commodity avg `-0.8953` n `12`; crypto_alt avg `-2.4705` n `228`; crypto_major avg `-3.1721` n `8`; equity avg `-2.0326` n `74`; fx avg `0.1072` n `6`; index avg `-1.2623` n `23`; metal avg `-1.4293` n `18`; unknown avg `-1.4487` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0487`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
