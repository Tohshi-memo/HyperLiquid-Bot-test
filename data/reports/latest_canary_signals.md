# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T13:37:33.847640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0559` n `12`; crypto_alt avg `0.0994` n `233`; crypto_major avg `0.2306` n `8`; equity avg `0.1138` n `136`; fx avg `0.0095` n `6`; index avg `-0.0159` n `27`; metal avg `-0.0418` n `20`; unknown avg `1.026` n `894`
- 1h: commodity avg `-0.275` n `12`; crypto_alt avg `-0.2024` n `233`; crypto_major avg `0.017` n `8`; equity avg `0.1376` n `136`; fx avg `0.0331` n `6`; index avg `0.0122` n `27`; metal avg `-0.0084` n `20`; unknown avg `3.8637` n `892`
- 4h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.2523` n `233`; crypto_major avg `0.1428` n `8`; equity avg `-0.1035` n `136`; fx avg `0.0656` n `6`; index avg `0.0016` n `27`; metal avg `0.042` n `20`; unknown avg `2.8798` n `886`
- 24h: commodity avg `0.4559` n `12`; crypto_alt avg `-0.3108` n `233`; crypto_major avg `1.8295` n `8`; equity avg `-0.935` n `136`; fx avg `0.0961` n `6`; index avg `-0.2467` n `27`; metal avg `-0.4786` n `20`; unknown avg `1.4892` n `650`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
