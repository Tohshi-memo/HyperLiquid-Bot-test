# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T18:37:36.148484+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3075` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.059` n `12`; crypto_alt avg `-0.5558` n `233`; crypto_major avg `-0.5869` n `8`; equity avg `-0.1953` n `137`; fx avg `0.0028` n `6`; index avg `-0.0032` n `27`; metal avg `-0.0446` n `20`; unknown avg `483.3687` n `918`
- 1h: commodity avg `-0.0223` n `12`; crypto_alt avg `-1.5605` n `233`; crypto_major avg `-1.2988` n `8`; equity avg `-0.3171` n `137`; fx avg `-0.0036` n `6`; index avg `0.0087` n `27`; metal avg `0.0583` n `20`; unknown avg `3.8922` n `915`
- 4h: commodity avg `0.1829` n `12`; crypto_alt avg `-0.6988` n `233`; crypto_major avg `-0.5541` n `8`; equity avg `-0.4777` n `137`; fx avg `0.0171` n `6`; index avg `-0.0164` n `27`; metal avg `0.1976` n `20`; unknown avg `-0.0508` n `889`
- 24h: commodity avg `0.7227` n `12`; crypto_alt avg `-3.7167` n `233`; crypto_major avg `-3.9051` n `8`; equity avg `-1.6073` n `137`; fx avg `0.2278` n `6`; index avg `-0.1817` n `27`; metal avg `0.0512` n `20`; unknown avg `0.5516` n `831`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
