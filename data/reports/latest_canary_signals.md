# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T00:07:23.784500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `12`; crypto_alt avg `0.1514` n `230`; crypto_major avg `0.233` n `8`; equity avg `0.2849` n `98`; fx avg `-0.0049` n `6`; index avg `0.0694` n `25`; metal avg `0.0598` n `20`; unknown avg `0.1091` n `771`
- 1h: commodity avg `-0.0134` n `12`; crypto_alt avg `0.3737` n `230`; crypto_major avg `0.4885` n `8`; equity avg `0.4849` n `98`; fx avg `0.0088` n `6`; index avg `0.0796` n `25`; metal avg `0.0787` n `20`; unknown avg `0.1971` n `771`
- 4h: commodity avg `-0.0061` n `12`; crypto_alt avg `0.1365` n `230`; crypto_major avg `0.2556` n `8`; equity avg `0.7488` n `98`; fx avg `-0.0168` n `6`; index avg `0.0946` n `25`; metal avg `0.0534` n `20`; unknown avg `-0.0319` n `771`
- 24h: commodity avg `0.4713` n `12`; crypto_alt avg `0.9721` n `230`; crypto_major avg `1.0175` n `8`; equity avg `5.1793` n `98`; fx avg `0.0373` n `6`; index avg `0.8924` n `25`; metal avg `0.8801` n `20`; unknown avg `0.4378` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0859`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0538`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0474`, n `666`, weak_sample_signal
