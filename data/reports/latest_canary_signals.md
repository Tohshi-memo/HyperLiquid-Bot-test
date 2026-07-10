# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T16:22:31.632497+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `12`; crypto_alt avg `0.0372` n `229`; crypto_major avg `0.0238` n `8`; equity avg `0.135` n `92`; fx avg `-0.0034` n `6`; index avg `0.0416` n `25`; metal avg `-0.03` n `20`; unknown avg `0.0186` n `765`
- 1h: commodity avg `-0.0069` n `12`; crypto_alt avg `0.0406` n `229`; crypto_major avg `0.0485` n `8`; equity avg `0.1953` n `92`; fx avg `-0.0218` n `6`; index avg `0.0418` n `25`; metal avg `0.0492` n `20`; unknown avg `-0.0784` n `765`
- 4h: commodity avg `-0.2858` n `12`; crypto_alt avg `-0.3282` n `229`; crypto_major avg `-0.6558` n `8`; equity avg `-0.4918` n `92`; fx avg `-0.0866` n `6`; index avg `0.0901` n `25`; metal avg `0.0836` n `20`; unknown avg `-0.192` n `765`
- 24h: commodity avg `-0.4392` n `12`; crypto_alt avg `1.1375` n `229`; crypto_major avg `1.3632` n `8`; equity avg `-0.7729` n `92`; fx avg `-0.1633` n `6`; index avg `0.0563` n `25`; metal avg `-0.2202` n `20`; unknown avg `-0.232` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
