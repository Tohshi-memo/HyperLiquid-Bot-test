# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T22:22:34.545697+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.1007` n `228`; crypto_major avg `-0.1681` n `8`; equity avg `-0.0476` n `86`; fx avg `0.0007` n `6`; index avg `0.0028` n `23`; metal avg `-0.0277` n `20`; unknown avg `-0.0925` n `765`
- 1h: commodity avg `0.032` n `12`; crypto_alt avg `0.3629` n `228`; crypto_major avg `0.4565` n `8`; equity avg `-0.2894` n `86`; fx avg `-0.0099` n `6`; index avg `-0.0415` n `23`; metal avg `-0.0914` n `20`; unknown avg `0.2413` n `765`
- 4h: commodity avg `-0.1277` n `12`; crypto_alt avg `0.4245` n `228`; crypto_major avg `0.3848` n `8`; equity avg `-0.2733` n `86`; fx avg `-0.0175` n `6`; index avg `-0.0665` n `23`; metal avg `-0.2519` n `20`; unknown avg `0.7104` n `765`
- 24h: commodity avg `0.401` n `12`; crypto_alt avg `-1.5256` n `228`; crypto_major avg `-1.5005` n `8`; equity avg `-2.5462` n `86`; fx avg `0.1044` n `6`; index avg `-0.2273` n `23`; metal avg `0.2141` n `20`; unknown avg `0.7089` n `700`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
