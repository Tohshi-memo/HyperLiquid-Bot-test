# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T08:22:30.486167+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `0.0211` n `228`; crypto_major avg `-0.0787` n `8`; equity avg `-0.0636` n `86`; fx avg `-0.0078` n `6`; index avg `-0.0099` n `23`; metal avg `0.0651` n `20`; unknown avg `0.0036` n `765`
- 1h: commodity avg `0.0491` n `12`; crypto_alt avg `0.0975` n `228`; crypto_major avg `-0.1902` n `8`; equity avg `-0.0136` n `86`; fx avg `-0.013` n `6`; index avg `-0.0176` n `23`; metal avg `0.2935` n `20`; unknown avg `-0.0195` n `757`
- 4h: commodity avg `0.2024` n `12`; crypto_alt avg `1.2345` n `228`; crypto_major avg `1.4086` n `8`; equity avg `0.4682` n `86`; fx avg `-0.0782` n `6`; index avg `0.0439` n `23`; metal avg `0.1203` n `20`; unknown avg `0.2061` n `733`
- 24h: commodity avg `-0.1685` n `12`; crypto_alt avg `-0.8953` n `228`; crypto_major avg `-0.6196` n `8`; equity avg `0.0038` n `86`; fx avg `-0.0428` n `6`; index avg `0.5012` n `23`; metal avg `-1.3675` n `20`; unknown avg `-0.7094` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
