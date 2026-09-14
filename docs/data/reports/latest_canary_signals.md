# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T14:01:18.086050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0465` n `12`; crypto_alt avg `-0.0366` n `233`; crypto_major avg `0.0584` n `8`; equity avg `0.1628` n `136`; fx avg `-0.011` n `6`; index avg `-0.0091` n `27`; metal avg `-0.0536` n `20`; unknown avg `0.1704` n `892`
- 1h: commodity avg `0.0343` n `12`; crypto_alt avg `0.7046` n `233`; crypto_major avg `0.8626` n `8`; equity avg `0.8691` n `136`; fx avg `0.0052` n `6`; index avg `0.1086` n `27`; metal avg `-0.0187` n `20`; unknown avg `1.6623` n `878`
- 4h: commodity avg `0.2201` n `12`; crypto_alt avg `-0.5926` n `233`; crypto_major avg `-0.1849` n `8`; equity avg `0.2907` n `136`; fx avg `0.0447` n `6`; index avg `0.044` n `27`; metal avg `-0.017` n `20`; unknown avg `0.4279` n `872`
- 24h: commodity avg `0.6643` n `12`; crypto_alt avg `-0.7865` n `233`; crypto_major avg `1.6162` n `8`; equity avg `-0.6962` n `136`; fx avg `0.074` n `6`; index avg `-0.2449` n `27`; metal avg `-0.5315` n `20`; unknown avg `1.1496` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
