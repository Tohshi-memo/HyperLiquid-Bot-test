# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T20:22:25.259374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `13`; crypto_alt avg `-0.1472` n `238`; crypto_major avg `-0.1487` n `8`; equity avg `-0.027` n `156`; fx avg `-0.01` n `6`; index avg `0.0046` n `27`; metal avg `0.0022` n `20`; unknown avg `1.2375` n `1263`
- 1h: commodity avg `0.0166` n `13`; crypto_alt avg `0.0077` n `238`; crypto_major avg `-0.1435` n `8`; equity avg `-0.0428` n `156`; fx avg `-0.0168` n `6`; index avg `-0.0038` n `27`; metal avg `-0.0058` n `20`; unknown avg `1.4312` n `1231`
- 4h: commodity avg `0.0488` n `13`; crypto_alt avg `-1.0288` n `238`; crypto_major avg `-0.6975` n `8`; equity avg `-0.2693` n `156`; fx avg `-0.0081` n `6`; index avg `-0.0514` n `27`; metal avg `-0.0199` n `20`; unknown avg `329.3791` n `1215`
- 24h: commodity avg `0.0684` n `13`; crypto_alt avg `-0.9014` n `238`; crypto_major avg `-0.5389` n `8`; equity avg `0.1899` n `156`; fx avg `-0.0075` n `6`; index avg `0.0469` n `27`; metal avg `0.0281` n `20`; unknown avg `3.9348` n `990`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
