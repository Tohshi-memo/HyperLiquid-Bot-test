# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T04:37:31.100016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0449` n `230`; crypto_major avg `-0.0251` n `8`; equity avg `-0.0743` n `98`; fx avg `-0.0144` n `6`; index avg `-0.0341` n `25`; metal avg `-0.0243` n `20`; unknown avg `-0.0686` n `771`
- 1h: commodity avg `0.0146` n `12`; crypto_alt avg `0.0139` n `230`; crypto_major avg `0.1712` n `8`; equity avg `-0.0372` n `98`; fx avg `-0.0046` n `6`; index avg `-0.0228` n `25`; metal avg `-0.0857` n `20`; unknown avg `-0.1679` n `771`
- 4h: commodity avg `0.113` n `12`; crypto_alt avg `-0.3453` n `230`; crypto_major avg `-0.3962` n `8`; equity avg `-0.7771` n `98`; fx avg `0.0432` n `6`; index avg `-0.1043` n `25`; metal avg `0.2792` n `20`; unknown avg `-0.4406` n `771`
- 24h: commodity avg `0.6137` n `12`; crypto_alt avg `0.0549` n `230`; crypto_major avg `0.0141` n `8`; equity avg `2.2923` n `98`; fx avg `0.0809` n `6`; index avg `0.264` n `25`; metal avg `0.7506` n `20`; unknown avg `0.2789` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0958`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0614`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0527`, n `666`, weak_sample_signal
