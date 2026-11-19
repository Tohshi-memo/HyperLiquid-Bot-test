# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T22:52:24.200545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1832` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `-0.1943` n `239`; crypto_major avg `-0.1468` n `8`; equity avg `-0.0416` n `165`; fx avg `0.0014` n `6`; index avg `0.0095` n `27`; metal avg `-0.0102` n `20`; unknown avg `158.5814` n `1262`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `0.4587` n `239`; crypto_major avg `0.595` n `8`; equity avg `0.4357` n `165`; fx avg `-0.0202` n `6`; index avg `0.0498` n `27`; metal avg `0.0336` n `20`; unknown avg `0.1603` n `1250`
- 4h: commodity avg `0.0235` n `13`; crypto_alt avg `-0.5191` n `239`; crypto_major avg `-1.3012` n `8`; equity avg `-2.0962` n `165`; fx avg `-0.0473` n `6`; index avg `-0.118` n `27`; metal avg `-0.4157` n `20`; unknown avg `5.0692` n `1230`
- 24h: commodity avg `0.102` n `13`; crypto_alt avg `0.3865` n `239`; crypto_major avg `0.5789` n `8`; equity avg `-2.8257` n `165`; fx avg `-0.0377` n `6`; index avg `-0.1399` n `27`; metal avg `-0.8031` n `20`; unknown avg `8.2533` n `1172`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
