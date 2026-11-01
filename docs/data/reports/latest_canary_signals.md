# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T01:52:25.855641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `13`; crypto_alt avg `-0.2501` n `238`; crypto_major avg `-0.1156` n `8`; equity avg `0.0015` n `156`; fx avg `-0.0043` n `6`; index avg `0.0002` n `27`; metal avg `0.0056` n `20`; unknown avg `-0.0815` n `1260`
- 1h: commodity avg `-0.0889` n `13`; crypto_alt avg `-0.0689` n `238`; crypto_major avg `-0.002` n `8`; equity avg `0.0539` n `156`; fx avg `-0.0007` n `6`; index avg `0.0006` n `27`; metal avg `0.0102` n `20`; unknown avg `0.5871` n `1254`
- 4h: commodity avg `0.0068` n `13`; crypto_alt avg `-0.1053` n `238`; crypto_major avg `0.0847` n `8`; equity avg `0.0304` n `156`; fx avg `-0.0016` n `6`; index avg `-0.0153` n `27`; metal avg `0.0184` n `20`; unknown avg `1.1459` n `1134`
- 24h: commodity avg `0.0448` n `13`; crypto_alt avg `-0.6787` n `238`; crypto_major avg `-0.2543` n `8`; equity avg `0.0283` n `156`; fx avg `0.0051` n `6`; index avg `-0.0844` n `27`; metal avg `0.0485` n `20`; unknown avg `1.8684` n `1004`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
