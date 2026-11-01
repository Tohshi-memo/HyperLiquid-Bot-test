# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T00:37:26.386427+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.166` n `238`; crypto_major avg `0.2221` n `8`; equity avg `0.0195` n `156`; fx avg `0.0031` n `6`; index avg `-0.0312` n `27`; metal avg `0.0006` n `20`; unknown avg `0.5395` n `1246`
- 1h: commodity avg `0.0671` n `13`; crypto_alt avg `0.0999` n `238`; crypto_major avg `0.2434` n `8`; equity avg `0.013` n `156`; fx avg `-0.0015` n `6`; index avg `-0.0227` n `27`; metal avg `0.0014` n `20`; unknown avg `0.0763` n `1204`
- 4h: commodity avg `0.1313` n `13`; crypto_alt avg `0.1599` n `238`; crypto_major avg `0.1717` n `8`; equity avg `0.0062` n `156`; fx avg `-0.0032` n `6`; index avg `-0.0218` n `27`; metal avg `0.0146` n `20`; unknown avg `0.3608` n `1078`
- 24h: commodity avg `0.0728` n `13`; crypto_alt avg `-0.9634` n `238`; crypto_major avg `-0.3713` n `8`; equity avg `-0.0289` n `156`; fx avg `0.0073` n `6`; index avg `-0.0953` n `27`; metal avg `0.026` n `20`; unknown avg `1.0346` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
