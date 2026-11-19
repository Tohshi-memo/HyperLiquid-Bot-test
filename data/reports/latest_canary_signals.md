# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T15:37:32.520786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0713` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0921` n `13`; crypto_alt avg `-0.4394` n `239`; crypto_major avg `-0.5204` n `8`; equity avg `-1.1444` n `165`; fx avg `0.0107` n `6`; index avg `-0.1403` n `27`; metal avg `-0.1018` n `20`; unknown avg `2.1401` n `1265`
- 1h: commodity avg `-0.2707` n `13`; crypto_alt avg `-1.1969` n `239`; crypto_major avg `-1.383` n `8`; equity avg `-2.7088` n `165`; fx avg `-0.0469` n `6`; index avg `-0.3117` n `27`; metal avg `-0.2479` n `20`; unknown avg `11.729` n `1263`
- 4h: commodity avg `0.1294` n `13`; crypto_alt avg `-1.3468` n `239`; crypto_major avg `-1.2722` n `8`; equity avg `-2.5238` n `165`; fx avg `-0.0568` n `6`; index avg `-0.347` n `27`; metal avg `-0.419` n `20`; unknown avg `11.2764` n `1257`
- 24h: commodity avg `0.1197` n `13`; crypto_alt avg `-0.1195` n `239`; crypto_major avg `0.0858` n `8`; equity avg `0.472` n `165`; fx avg `0.0059` n `6`; index avg `0.1229` n `27`; metal avg `-0.4113` n `20`; unknown avg `1.5833` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
