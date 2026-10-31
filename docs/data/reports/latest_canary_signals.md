# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T21:07:26.624177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `13`; crypto_alt avg `0.0145` n `238`; crypto_major avg `-0.0312` n `8`; equity avg `-0.0087` n `156`; fx avg `-0.0146` n `6`; index avg `-0.0011` n `27`; metal avg `-0.004` n `20`; unknown avg `-0.1707` n `1248`
- 1h: commodity avg `0.0378` n `13`; crypto_alt avg `-0.0815` n `238`; crypto_major avg `-0.1842` n `8`; equity avg `0.0027` n `156`; fx avg `-0.0047` n `6`; index avg `-0.0083` n `27`; metal avg `-0.0041` n `20`; unknown avg `-0.0544` n `1222`
- 4h: commodity avg `0.0282` n `13`; crypto_alt avg `-0.6497` n `238`; crypto_major avg `-0.0255` n `8`; equity avg `0.0403` n `156`; fx avg `-0.0094` n `6`; index avg `-0.0` n `27`; metal avg `-0.017` n `20`; unknown avg `0.4037` n `1156`
- 24h: commodity avg `-0.0627` n `13`; crypto_alt avg `0.4842` n `238`; crypto_major avg `0.1582` n `8`; equity avg `0.2085` n `156`; fx avg `-0.0542` n `6`; index avg `-0.0469` n `27`; metal avg `0.069` n `20`; unknown avg `1.6516` n `1077`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
