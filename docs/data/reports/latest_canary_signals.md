# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T14:37:29.050097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.03` n `12`; crypto_alt avg `-0.1425` n `233`; crypto_major avg `-0.1291` n `8`; equity avg `-0.3144` n `136`; fx avg `-0.0054` n `6`; index avg `-0.058` n `27`; metal avg `-0.0047` n `20`; unknown avg `-0.1441` n `894`
- 1h: commodity avg `0.1201` n `12`; crypto_alt avg `0.0994` n `233`; crypto_major avg `0.0532` n `8`; equity avg `0.2735` n `136`; fx avg `-0.0325` n `6`; index avg `-0.0275` n `27`; metal avg `-0.0584` n `20`; unknown avg `0.1678` n `878`
- 4h: commodity avg `0.1581` n `12`; crypto_alt avg `-0.5062` n `233`; crypto_major avg `-0.1162` n `8`; equity avg `-0.1625` n `136`; fx avg `0.027` n `6`; index avg `-0.0844` n `27`; metal avg `-0.0982` n `20`; unknown avg `0.9924` n `872`
- 24h: commodity avg `0.7324` n `12`; crypto_alt avg `-0.8922` n `233`; crypto_major avg `1.1385` n `8`; equity avg `-1.0373` n `136`; fx avg `0.0551` n `6`; index avg `-0.3293` n `27`; metal avg `-0.5669` n `20`; unknown avg `1.3481` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
