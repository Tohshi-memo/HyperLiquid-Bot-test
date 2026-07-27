# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T21:34:13.670078+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0177` n `12`; crypto_alt avg `-0.1644` n `230`; crypto_major avg `-0.0985` n `8`; equity avg `-0.0117` n `102`; fx avg `-0.0011` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0036` n `20`; unknown avg `0.1842` n `774`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `-0.2034` n `230`; crypto_major avg `-0.2792` n `8`; equity avg `0.0175` n `102`; fx avg `-0.009` n `6`; index avg `-0.0306` n `25`; metal avg `0.0096` n `20`; unknown avg `3.7255` n `774`
- 4h: commodity avg `-0.1443` n `12`; crypto_alt avg `-0.1653` n `230`; crypto_major avg `-0.3783` n `8`; equity avg `0.9671` n `102`; fx avg `0.0052` n `6`; index avg `0.1579` n `25`; metal avg `0.0389` n `20`; unknown avg `98.6543` n `774`
- 24h: commodity avg `-0.971` n `12`; crypto_alt avg `-1.1812` n `230`; crypto_major avg `-0.6143` n `8`; equity avg `-0.9749` n `102`; fx avg `-0.0417` n `6`; index avg `-0.3383` n `25`; metal avg `0.1485` n `20`; unknown avg `97.6242` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
