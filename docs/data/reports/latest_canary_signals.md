# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T18:37:31.040696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0136` n `13`; crypto_alt avg `0.0437` n `238`; crypto_major avg `0.1264` n `8`; equity avg `0.0232` n `156`; fx avg `0.0077` n `6`; index avg `-0.0083` n `27`; metal avg `0.0044` n `20`; unknown avg `-0.0152` n `1263`
- 1h: commodity avg `-0.0083` n `13`; crypto_alt avg `-0.3912` n `238`; crypto_major avg `-0.2282` n `8`; equity avg `-0.1317` n `156`; fx avg `0.0155` n `6`; index avg `-0.0255` n `27`; metal avg `0.007` n `20`; unknown avg `160.6687` n `1249`
- 4h: commodity avg `-0.0777` n `13`; crypto_alt avg `-0.7718` n `238`; crypto_major avg `-0.2683` n `8`; equity avg `-0.0979` n `156`; fx avg `0.0317` n `6`; index avg `0.0019` n `27`; metal avg `0.0172` n `20`; unknown avg `-0.3441` n `1237`
- 24h: commodity avg `-0.02` n `13`; crypto_alt avg `-0.6778` n `238`; crypto_major avg `-0.1581` n `8`; equity avg `0.2995` n `156`; fx avg `0.012` n `6`; index avg `0.0574` n `27`; metal avg `0.0685` n `20`; unknown avg `3.5125` n `1004`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1413`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
