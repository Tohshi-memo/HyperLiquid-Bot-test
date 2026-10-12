# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T18:52:33.202228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0575` n `13`; crypto_alt avg `-0.019` n `235`; crypto_major avg `-0.014` n `8`; equity avg `-0.1092` n `151`; fx avg `0.0025` n `6`; index avg `-0.0126` n `26`; metal avg `-0.0133` n `20`; unknown avg `-0.0646` n `1134`
- 1h: commodity avg `0.0055` n `13`; crypto_alt avg `-0.2254` n `235`; crypto_major avg `-0.1939` n `8`; equity avg `-0.1467` n `151`; fx avg `0.0004` n `6`; index avg `-0.0251` n `26`; metal avg `-0.0092` n `20`; unknown avg `-0.6038` n `1132`
- 4h: commodity avg `0.061` n `13`; crypto_alt avg `-0.6208` n `235`; crypto_major avg `-0.5619` n `8`; equity avg `-0.4781` n `151`; fx avg `-0.0517` n `6`; index avg `-0.0295` n `26`; metal avg `-0.0072` n `20`; unknown avg `0.703` n `1126`
- 24h: commodity avg `0.4745` n `13`; crypto_alt avg `-2.8516` n `235`; crypto_major avg `-1.9857` n `8`; equity avg `-3.5489` n `151`; fx avg `-0.1707` n `6`; index avg `-0.3539` n `26`; metal avg `-0.1656` n `20`; unknown avg `0.2687` n `881`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2138`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1817`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1242`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1004`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0852`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0836`, n `666`, weak_sample_signal
