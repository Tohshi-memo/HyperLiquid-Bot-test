# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T23:22:24.854400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0437` n `13`; crypto_alt avg `0.1707` n `238`; crypto_major avg `0.1992` n `8`; equity avg `0.2413` n `156`; fx avg `-0.0068` n `6`; index avg `0.0391` n `27`; metal avg `0.0606` n `20`; unknown avg `0.2012` n `1263`
- 1h: commodity avg `-0.0167` n `13`; crypto_alt avg `0.4564` n `238`; crypto_major avg `0.5512` n `8`; equity avg `0.1184` n `156`; fx avg `0.0172` n `6`; index avg `0.0068` n `27`; metal avg `0.0983` n `20`; unknown avg `161.3295` n `1241`
- 4h: commodity avg `0.0054` n `13`; crypto_alt avg `0.4513` n `238`; crypto_major avg `0.2563` n `8`; equity avg `0.1146` n `156`; fx avg `-0.0003` n `6`; index avg `0.0035` n `27`; metal avg `0.0868` n `20`; unknown avg `2.0211` n `1199`
- 24h: commodity avg `-0.0063` n `13`; crypto_alt avg `-0.4055` n `238`; crypto_major avg `0.0581` n `8`; equity avg `0.3587` n `156`; fx avg `0.0127` n `6`; index avg `0.0425` n `27`; metal avg `0.1126` n `20`; unknown avg `3.4834` n `1084`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
