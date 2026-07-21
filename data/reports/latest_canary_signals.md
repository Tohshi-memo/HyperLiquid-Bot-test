# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T23:52:27.289287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0052` n `12`; crypto_alt avg `0.0341` n `230`; crypto_major avg `0.0856` n `8`; equity avg `0.0211` n `98`; fx avg `0.0079` n `6`; index avg `0.0119` n `25`; metal avg `0.0055` n `20`; unknown avg `0.063` n `771`
- 1h: commodity avg `0.013` n `12`; crypto_alt avg `0.1045` n `230`; crypto_major avg `0.1587` n `8`; equity avg `0.1987` n `98`; fx avg `0.0155` n `6`; index avg `0.0147` n `25`; metal avg `0.0244` n `20`; unknown avg `-0.0427` n `771`
- 4h: commodity avg `0.041` n `12`; crypto_alt avg `-0.0483` n `230`; crypto_major avg `-0.0287` n `8`; equity avg `0.6108` n `98`; fx avg `-0.0093` n `6`; index avg `0.0127` n `25`; metal avg `-0.0102` n `20`; unknown avg `-0.1596` n `771`
- 24h: commodity avg `0.4869` n `12`; crypto_alt avg `0.8705` n `230`; crypto_major avg `0.7362` n `8`; equity avg `4.5126` n `98`; fx avg `0.0583` n `6`; index avg `0.7356` n `25`; metal avg `0.7817` n `20`; unknown avg `0.4023` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0868`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0528`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0473`, n `666`, weak_sample_signal
