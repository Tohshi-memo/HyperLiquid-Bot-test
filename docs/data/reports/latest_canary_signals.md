# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T11:07:37.006823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1201` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0587` n `13`; crypto_alt avg `-0.3955` n `235`; crypto_major avg `-0.2395` n `8`; equity avg `-0.694` n `151`; fx avg `0.0023` n `6`; index avg `-0.0128` n `26`; metal avg `0.0127` n `20`; unknown avg `-0.2602` n `1133`
- 1h: commodity avg `0.0913` n `13`; crypto_alt avg `-0.8873` n `235`; crypto_major avg `-0.62` n `8`; equity avg `-0.4672` n `151`; fx avg `0.0372` n `6`; index avg `-0.0645` n `26`; metal avg `-0.0473` n `20`; unknown avg `0.1407` n `1133`
- 4h: commodity avg `-0.0976` n `13`; crypto_alt avg `-1.9012` n `235`; crypto_major avg `-1.1031` n `8`; equity avg `-0.0078` n `151`; fx avg `-0.003` n `6`; index avg `0.017` n `26`; metal avg `-0.021` n `20`; unknown avg `0.2781` n `1117`
- 24h: commodity avg `-0.0218` n `13`; crypto_alt avg `-4.6006` n `235`; crypto_major avg `-2.7357` n `8`; equity avg `-3.0346` n `151`; fx avg `0.0731` n `6`; index avg `-0.3479` n `26`; metal avg `-0.0221` n `20`; unknown avg `0.5324` n `989`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1731`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1678`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1604`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.146`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
