# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T02:52:28.766241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1879` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0372` n `13`; crypto_alt avg `-0.4267` n `239`; crypto_major avg `-0.5046` n `8`; equity avg `-0.3756` n `166`; fx avg `0.003` n `6`; index avg `-0.0362` n `27`; metal avg `-0.1576` n `20`; unknown avg `158.0831` n `1266`
- 1h: commodity avg `-0.0342` n `13`; crypto_alt avg `-0.8315` n `239`; crypto_major avg `-1.2027` n `8`; equity avg `-0.5452` n `166`; fx avg `-0.0537` n `6`; index avg `-0.0148` n `27`; metal avg `-0.3265` n `20`; unknown avg `159.4617` n `1262`
- 4h: commodity avg `-0.0909` n `13`; crypto_alt avg `0.2169` n `239`; crypto_major avg `-0.6983` n `8`; equity avg `-0.748` n `166`; fx avg `0.0315` n `6`; index avg `0.0387` n `27`; metal avg `-0.1871` n `20`; unknown avg `0.8879` n `1250`
- 24h: commodity avg `-1.1628` n `13`; crypto_alt avg `1.3732` n `239`; crypto_major avg `0.795` n `8`; equity avg `6.0855` n `166`; fx avg `-0.2492` n `6`; index avg `0.7551` n `27`; metal avg `0.3743` n `20`; unknown avg `2.5014` n `1045`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
