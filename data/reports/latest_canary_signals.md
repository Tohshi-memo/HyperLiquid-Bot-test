# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T10:52:26.837335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1041` n `13`; crypto_alt avg `0.0093` n `239`; crypto_major avg `0.1088` n `8`; equity avg `0.0953` n `164`; fx avg `0.0015` n `6`; index avg `0.0192` n `27`; metal avg `0.0313` n `20`; unknown avg `-0.1928` n `1266`
- 1h: commodity avg `0.0607` n `13`; crypto_alt avg `-0.1922` n `239`; crypto_major avg `-0.0729` n `8`; equity avg `0.2164` n `164`; fx avg `0.0336` n `6`; index avg `-0.0048` n `27`; metal avg `0.0024` n `20`; unknown avg `0.1709` n `1264`
- 4h: commodity avg `0.0472` n `13`; crypto_alt avg `0.1322` n `239`; crypto_major avg `0.0458` n `8`; equity avg `0.8529` n `164`; fx avg `0.1288` n `6`; index avg `0.1697` n `27`; metal avg `0.0257` n `20`; unknown avg `286.668` n `1222`
- 24h: commodity avg `0.2262` n `13`; crypto_alt avg `-0.0491` n `239`; crypto_major avg `-0.389` n `8`; equity avg `0.4353` n `164`; fx avg `0.0623` n `6`; index avg `0.2286` n `27`; metal avg `-0.183` n `20`; unknown avg `3.9483` n `1161`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
