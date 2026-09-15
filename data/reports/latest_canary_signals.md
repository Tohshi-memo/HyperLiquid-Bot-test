# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T16:22:33.357771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0743` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.1452` n `233`; crypto_major avg `0.1356` n `8`; equity avg `0.0347` n `137`; fx avg `-0.0242` n `6`; index avg `0.0145` n `27`; metal avg `0.0406` n `20`; unknown avg `0.0044` n `909`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `0.0655` n `233`; crypto_major avg `0.1327` n `8`; equity avg `0.0397` n `137`; fx avg `-0.0158` n `6`; index avg `0.0094` n `27`; metal avg `0.1121` n `20`; unknown avg `0.1205` n `907`
- 4h: commodity avg `0.2434` n `12`; crypto_alt avg `-0.9543` n `233`; crypto_major avg `-1.2306` n `8`; equity avg `-0.8624` n `137`; fx avg `0.0269` n `6`; index avg `-0.1563` n `27`; metal avg `0.1241` n `20`; unknown avg `1.4486` n `873`
- 24h: commodity avg `0.2677` n `12`; crypto_alt avg `-2.3419` n `233`; crypto_major avg `-2.6384` n `8`; equity avg `-1.1663` n `137`; fx avg `0.2366` n `6`; index avg `-0.1557` n `27`; metal avg `0.0049` n `20`; unknown avg `0.3062` n `813`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
