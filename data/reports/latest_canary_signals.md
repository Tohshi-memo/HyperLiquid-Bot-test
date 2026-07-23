# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T08:07:27.386532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0807` n `12`; crypto_alt avg `0.0804` n `230`; crypto_major avg `0.1423` n `8`; equity avg `0.257` n `98`; fx avg `-0.008` n `6`; index avg `0.0527` n `25`; metal avg `0.0591` n `20`; unknown avg `0.0377` n `773`
- 1h: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.1511` n `230`; crypto_major avg `-0.173` n `8`; equity avg `0.0396` n `98`; fx avg `0.0086` n `6`; index avg `-0.0097` n `25`; metal avg `-0.1052` n `20`; unknown avg `0.1468` n `773`
- 4h: commodity avg `0.1451` n `12`; crypto_alt avg `0.198` n `230`; crypto_major avg `-0.1503` n `8`; equity avg `0.0843` n `98`; fx avg `0.0409` n `6`; index avg `-0.0082` n `25`; metal avg `-0.3404` n `20`; unknown avg `-0.2289` n `741`
- 24h: commodity avg `0.5984` n `12`; crypto_alt avg `-0.1617` n `230`; crypto_major avg `-0.1346` n `8`; equity avg `0.4401` n `98`; fx avg `-0.0652` n `6`; index avg `0.142` n `25`; metal avg `-0.2454` n `20`; unknown avg `11.4274` n `741`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
