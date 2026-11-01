# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T17:22:26.485376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `-0.0917` n `238`; crypto_major avg `-0.006` n `8`; equity avg `-0.0146` n `156`; fx avg `0.0015` n `6`; index avg `0.0005` n `27`; metal avg `-0.0013` n `20`; unknown avg `1.2466` n `1263`
- 1h: commodity avg `0.0071` n `13`; crypto_alt avg `-0.183` n `238`; crypto_major avg `-0.0549` n `8`; equity avg `-0.0054` n `156`; fx avg `-0.0036` n `6`; index avg `-0.0013` n `27`; metal avg `0.0117` n `20`; unknown avg `160.8167` n `1257`
- 4h: commodity avg `-0.0377` n `13`; crypto_alt avg `-0.6324` n `238`; crypto_major avg `-0.0761` n `8`; equity avg `-0.0041` n `156`; fx avg `0.0149` n `6`; index avg `0.0563` n `27`; metal avg `-0.0027` n `20`; unknown avg `1.6457` n `1245`
- 24h: commodity avg `0.0264` n `13`; crypto_alt avg `-0.5298` n `238`; crypto_major avg `0.178` n `8`; equity avg `0.4739` n `156`; fx avg `-0.002` n `6`; index avg `0.0968` n `27`; metal avg `0.0512` n `20`; unknown avg `5.897` n `1012`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
