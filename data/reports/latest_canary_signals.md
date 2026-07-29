# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T17:07:25.573669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.99` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.0088` n `230`; crypto_major avg `0.1106` n `8`; equity avg `0.4589` n `102`; fx avg `0.0131` n `6`; index avg `0.0708` n `25`; metal avg `0.1764` n `20`; unknown avg `0.0183` n `778`
- 1h: commodity avg `-0.0425` n `12`; crypto_alt avg `0.1159` n `230`; crypto_major avg `0.1208` n `8`; equity avg `0.9415` n `102`; fx avg `0.0327` n `6`; index avg `0.189` n `25`; metal avg `0.2675` n `20`; unknown avg `0.0702` n `778`
- 4h: commodity avg `0.1961` n `12`; crypto_alt avg `-0.4636` n `230`; crypto_major avg `-0.4141` n `8`; equity avg `-1.8516` n `102`; fx avg `-0.0129` n `6`; index avg `-0.2314` n `25`; metal avg `0.1701` n `20`; unknown avg `0.1917` n `777`
- 24h: commodity avg `1.413` n `12`; crypto_alt avg `-2.6031` n `230`; crypto_major avg `-0.6975` n `8`; equity avg `-2.0339` n `102`; fx avg `-0.08` n `6`; index avg `-0.4558` n `25`; metal avg `-0.0837` n `20`; unknown avg `-0.0784` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
