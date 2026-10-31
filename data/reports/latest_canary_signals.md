# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T19:22:28.845247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0207` n `13`; crypto_alt avg `-0.1505` n `238`; crypto_major avg `-0.1057` n `8`; equity avg `-0.0227` n `156`; fx avg `0.0013` n `6`; index avg `0.0036` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.2771` n `1262`
- 1h: commodity avg `0.0005` n `13`; crypto_alt avg `-0.1666` n `238`; crypto_major avg `-0.1048` n `8`; equity avg `-0.0051` n `156`; fx avg `-0.0054` n `6`; index avg `-0.0051` n `27`; metal avg `0.0049` n `20`; unknown avg `-0.3169` n `1254`
- 4h: commodity avg `0.0017` n `13`; crypto_alt avg `-0.2231` n `238`; crypto_major avg `0.267` n `8`; equity avg `0.054` n `156`; fx avg `-0.0191` n `6`; index avg `0.0018` n `27`; metal avg `-0.0016` n `20`; unknown avg `0.3188` n `1196`
- 24h: commodity avg `-0.3121` n `13`; crypto_alt avg `1.4631` n `238`; crypto_major avg `0.7134` n `8`; equity avg `1.0248` n `156`; fx avg `-0.0331` n `6`; index avg `0.0609` n `27`; metal avg `0.1409` n `20`; unknown avg `0.8698` n `1041`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
