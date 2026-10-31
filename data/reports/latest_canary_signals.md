# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T18:37:25.037249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0022` n `13`; crypto_alt avg `-0.0102` n `238`; crypto_major avg `-0.0263` n `8`; equity avg `-0.0044` n `156`; fx avg `0.0062` n `6`; index avg `0.0056` n `27`; metal avg `0.0024` n `20`; unknown avg `197.9366` n `1262`
- 1h: commodity avg `0.033` n `13`; crypto_alt avg `-0.0222` n `238`; crypto_major avg `0.1758` n `8`; equity avg `0.0531` n `156`; fx avg `-0.0016` n `6`; index avg `0.016` n `27`; metal avg `-0.0099` n `20`; unknown avg `-0.4583` n `1216`
- 4h: commodity avg `-0.0036` n `13`; crypto_alt avg `0.4912` n `238`; crypto_major avg `0.4839` n `8`; equity avg `0.1191` n `156`; fx avg `-0.0001` n `6`; index avg `0.017` n `27`; metal avg `0.0103` n `20`; unknown avg `0.4052` n `1196`
- 24h: commodity avg `-0.3437` n `13`; crypto_alt avg `1.7767` n `238`; crypto_major avg `0.9081` n `8`; equity avg `1.7617` n `156`; fx avg `-0.0119` n `6`; index avg `0.1292` n `27`; metal avg `0.1544` n `20`; unknown avg `1.1048` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1346`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
