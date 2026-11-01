# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T02:22:32.410989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0679` n `13`; crypto_alt avg `-0.2083` n `238`; crypto_major avg `-0.1228` n `8`; equity avg `-0.0522` n `156`; fx avg `-0.0006` n `6`; index avg `-0.0017` n `27`; metal avg `0.0038` n `20`; unknown avg `0.0748` n `1262`
- 1h: commodity avg `-0.0255` n `13`; crypto_alt avg `-0.2323` n `238`; crypto_major avg `-0.0817` n `8`; equity avg `-0.0175` n `156`; fx avg `-0.0027` n `6`; index avg `0.0037` n `27`; metal avg `0.004` n `20`; unknown avg `-0.0811` n `1254`
- 4h: commodity avg `-0.0137` n `13`; crypto_alt avg `-0.2757` n `238`; crypto_major avg `-0.0825` n `8`; equity avg `-0.0196` n `156`; fx avg `0.0015` n `6`; index avg `-0.0144` n `27`; metal avg `0.0073` n `20`; unknown avg `0.8317` n `1200`
- 24h: commodity avg `-0.1134` n `13`; crypto_alt avg `-0.6219` n `238`; crypto_major avg `-0.3838` n `8`; equity avg `0.0354` n `156`; fx avg `0.0022` n `6`; index avg `-0.0743` n `27`; metal avg `0.0547` n `20`; unknown avg `1.8732` n `1006`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
