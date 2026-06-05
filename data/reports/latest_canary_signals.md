# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T00:52:21.604964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.1553` n `228`; crypto_major avg `-0.2263` n `8`; equity avg `-0.1037` n `74`; fx avg `0.0141` n `6`; index avg `-0.1332` n `23`; metal avg `-0.1253` n `18`; unknown avg `-0.2422` n `424`
- 1h: commodity avg `-0.127` n `12`; crypto_alt avg `-0.1411` n `228`; crypto_major avg `-0.276` n `8`; equity avg `-0.6526` n `74`; fx avg `0.0729` n `6`; index avg `-0.5037` n `23`; metal avg `-0.3642` n `18`; unknown avg `0.0349` n `424`
- 4h: commodity avg `-0.1087` n `12`; crypto_alt avg `-1.2377` n `228`; crypto_major avg `-0.7573` n `8`; equity avg `-1.2386` n `74`; fx avg `0.0784` n `6`; index avg `-0.7734` n `23`; metal avg `-0.5276` n `18`; unknown avg `-0.9355` n `424`
- 24h: commodity avg `-0.5847` n `12`; crypto_alt avg `-5.4195` n `228`; crypto_major avg `-2.9754` n `8`; equity avg `-1.4365` n `73`; fx avg `0.1629` n `6`; index avg `-0.5552` n `23`; metal avg `0.0772` n `18`; unknown avg `-1.1453` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
