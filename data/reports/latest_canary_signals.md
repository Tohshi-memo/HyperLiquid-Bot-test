# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T10:07:27.527449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0844` n `12`; crypto_alt avg `-0.1261` n `230`; crypto_major avg `-0.0455` n `8`; equity avg `-0.0508` n `100`; fx avg `-0.0036` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.0009` n `773`
- 1h: commodity avg `0.0309` n `12`; crypto_alt avg `-0.0492` n `230`; crypto_major avg `-0.0028` n `8`; equity avg `0.2226` n `100`; fx avg `-0.0188` n `6`; index avg `0.0262` n `25`; metal avg `0.058` n `20`; unknown avg `0.133` n `773`
- 4h: commodity avg `-0.3141` n `12`; crypto_alt avg `0.0024` n `230`; crypto_major avg `0.115` n `8`; equity avg `0.7237` n `100`; fx avg `-0.0317` n `6`; index avg `0.1572` n `25`; metal avg `0.3806` n `20`; unknown avg `0.2814` n `772`
- 24h: commodity avg `-0.1855` n `12`; crypto_alt avg `-1.0765` n `230`; crypto_major avg `-1.5126` n `8`; equity avg `-1.5447` n `99`; fx avg `-0.1444` n `6`; index avg `-0.4233` n `25`; metal avg `-0.2805` n `20`; unknown avg `0.2311` n `756`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0966`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.083`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0811`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
