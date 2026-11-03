# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T13:07:28.917039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1479` n `13`; crypto_alt avg `-0.3333` n `239`; crypto_major avg `-0.2743` n `8`; equity avg `-0.0822` n `157`; fx avg `0.0095` n `6`; index avg `-0.0159` n `27`; metal avg `0.0163` n `20`; unknown avg `0.3379` n `1258`
- 1h: commodity avg `-0.251` n `13`; crypto_alt avg `0.6681` n `239`; crypto_major avg `0.587` n `8`; equity avg `0.5794` n `157`; fx avg `-0.0165` n `6`; index avg `0.0758` n `27`; metal avg `0.3096` n `20`; unknown avg `3.63` n `1256`
- 4h: commodity avg `-0.1455` n `13`; crypto_alt avg `1.4916` n `239`; crypto_major avg `0.9149` n `8`; equity avg `0.6974` n `157`; fx avg `0.003` n `6`; index avg `0.0662` n `27`; metal avg `0.3708` n `20`; unknown avg `164.9675` n `1222`
- 24h: commodity avg `-0.4141` n `13`; crypto_alt avg `-0.4088` n `238`; crypto_major avg `-0.0722` n `8`; equity avg `-2.5936` n `157`; fx avg `-0.0032` n `6`; index avg `-0.1619` n `27`; metal avg `-0.1324` n `20`; unknown avg `0.167` n `1022`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
