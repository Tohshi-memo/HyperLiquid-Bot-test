# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T03:37:27.719578+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `12`; crypto_alt avg `0.1088` n `230`; crypto_major avg `0.1381` n `8`; equity avg `0.1934` n `107`; fx avg `0.0199` n `6`; index avg `0.0268` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.0521` n `781`
- 1h: commodity avg `-0.0425` n `12`; crypto_alt avg `-0.211` n `230`; crypto_major avg `-0.1914` n `8`; equity avg `0.0447` n `107`; fx avg `0.036` n `6`; index avg `-0.0411` n `25`; metal avg `0.0505` n `20`; unknown avg `0.1432` n `780`
- 4h: commodity avg `0.2274` n `12`; crypto_alt avg `0.2201` n `230`; crypto_major avg `0.3307` n `8`; equity avg `-0.3026` n `107`; fx avg `0.0183` n `6`; index avg `-0.0869` n `25`; metal avg `0.2119` n `20`; unknown avg `-0.2923` n `780`
- 24h: commodity avg `0.2414` n `12`; crypto_alt avg `1.1322` n `230`; crypto_major avg `1.0501` n `8`; equity avg `1.6142` n `107`; fx avg `0.0269` n `6`; index avg `0.1213` n `25`; metal avg `0.0401` n `20`; unknown avg `0.2342` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
