# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T04:07:23.720917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0685` n `233`; crypto_major avg `0.0251` n `8`; equity avg `-0.0902` n `136`; fx avg `-0.0015` n `6`; index avg `-0.0239` n `27`; metal avg `0.0021` n `20`; unknown avg `0.3936` n `904`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `-0.3129` n `233`; crypto_major avg `-0.0884` n `8`; equity avg `-0.2173` n `136`; fx avg `-0.0173` n `6`; index avg `-0.042` n `27`; metal avg `-0.0299` n `20`; unknown avg `-0.1922` n `896`
- 4h: commodity avg `0.0977` n `12`; crypto_alt avg `-0.6146` n `233`; crypto_major avg `-0.3822` n `8`; equity avg `-0.0249` n `136`; fx avg `0.0746` n `6`; index avg `0.0254` n `27`; metal avg `0.1643` n `20`; unknown avg `-0.2534` n `890`
- 24h: commodity avg `-0.0425` n `12`; crypto_alt avg `-0.8671` n `233`; crypto_major avg `0.2487` n `8`; equity avg `-0.2344` n `136`; fx avg `0.1105` n `6`; index avg `-0.0418` n `27`; metal avg `-0.2317` n `20`; unknown avg `4.9513` n `788`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
