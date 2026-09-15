# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T15:07:29.705412+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2239` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0537` n `12`; crypto_alt avg `0.9353` n `233`; crypto_major avg `0.8064` n `8`; equity avg `0.2449` n `137`; fx avg `0.0046` n `6`; index avg `0.0244` n `27`; metal avg `0.0262` n `20`; unknown avg `0.4259` n `907`
- 1h: commodity avg `0.1673` n `12`; crypto_alt avg `-0.5616` n `233`; crypto_major avg `-0.8805` n `8`; equity avg `-0.6088` n `137`; fx avg `0.0336` n `6`; index avg `-0.0814` n `27`; metal avg `-0.199` n `20`; unknown avg `0.4093` n `895`
- 4h: commodity avg `0.3891` n `12`; crypto_alt avg `-0.9477` n `233`; crypto_major avg `-1.3617` n `8`; equity avg `-0.9671` n `137`; fx avg `0.0562` n `6`; index avg `-0.1378` n `27`; metal avg `-0.0223` n `20`; unknown avg `1.3696` n `873`
- 24h: commodity avg `0.3115` n `12`; crypto_alt avg `-1.6918` n `233`; crypto_major avg `-1.9669` n `8`; equity avg `-0.5228` n `137`; fx avg `0.2262` n `6`; index avg `-0.0112` n `27`; metal avg `0.0077` n `20`; unknown avg `0.1496` n `813`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
