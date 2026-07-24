# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T09:52:28.237433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `0.1432` n `230`; crypto_major avg `0.1587` n `8`; equity avg `0.1189` n `100`; fx avg `-0.0106` n `6`; index avg `0.0039` n `25`; metal avg `0.0179` n `20`; unknown avg `0.0224` n `773`
- 1h: commodity avg `-0.0779` n `12`; crypto_alt avg `0.0021` n `230`; crypto_major avg `-0.1275` n `8`; equity avg `0.3261` n `100`; fx avg `-0.0198` n `6`; index avg `0.0411` n `25`; metal avg `0.0559` n `20`; unknown avg `0.1296` n `773`
- 4h: commodity avg `-0.4664` n `12`; crypto_alt avg `0.1959` n `230`; crypto_major avg `0.2529` n `8`; equity avg `0.6019` n `100`; fx avg `-0.0385` n `6`; index avg `0.0998` n `25`; metal avg `0.3204` n `20`; unknown avg `0.2211` n `756`
- 24h: commodity avg `-0.3068` n `12`; crypto_alt avg `-0.9657` n `230`; crypto_major avg `-1.4231` n `8`; equity avg `-1.5758` n `99`; fx avg `-0.1507` n `6`; index avg `-0.4214` n `25`; metal avg `-0.3381` n `20`; unknown avg `0.2204` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0971`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0857`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0805`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
