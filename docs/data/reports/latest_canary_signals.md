# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T16:37:27.865553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1711` n `12`; crypto_alt avg `-0.759` n `228`; crypto_major avg `-1.1959` n `8`; equity avg `-0.4216` n `74`; fx avg `0.0039` n `6`; index avg `-0.3347` n `23`; metal avg `-0.0673` n `18`; unknown avg `-0.4815` n `424`
- 1h: commodity avg `-0.4234` n `12`; crypto_alt avg `0.3345` n `228`; crypto_major avg `0.3234` n `8`; equity avg `-0.9447` n `74`; fx avg `-0.0278` n `6`; index avg `-0.7276` n `23`; metal avg `-0.2024` n `18`; unknown avg `-0.0752` n `424`
- 4h: commodity avg `-1.453` n `12`; crypto_alt avg `-1.8825` n `228`; crypto_major avg `-2.3918` n `8`; equity avg `-3.7548` n `74`; fx avg `-0.1646` n `6`; index avg `-2.1096` n `23`; metal avg `-3.256` n `18`; unknown avg `-1.1842` n `424`
- 24h: commodity avg `-1.6289` n `12`; crypto_alt avg `-8.6777` n `228`; crypto_major avg `-6.8485` n `8`; equity avg `-5.8679` n `74`; fx avg `-0.0568` n `6`; index avg `-3.0809` n `23`; metal avg `-4.1361` n `18`; unknown avg `-1.4864` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
