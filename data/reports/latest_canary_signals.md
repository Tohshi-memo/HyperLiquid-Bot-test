# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T07:37:26.101752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2739` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0454` n `13`; crypto_alt avg `-0.015` n `239`; crypto_major avg `-0.0227` n `8`; equity avg `-0.2671` n `158`; fx avg `0.0161` n `6`; index avg `-0.0479` n `27`; metal avg `-0.0449` n `20`; unknown avg `-0.1239` n `1255`
- 1h: commodity avg `-0.1421` n `13`; crypto_alt avg `-0.6126` n `239`; crypto_major avg `-0.4556` n `8`; equity avg `-0.7006` n `158`; fx avg `0.008` n `6`; index avg `-0.0925` n `27`; metal avg `-0.141` n `20`; unknown avg `-0.0847` n `1249`
- 4h: commodity avg `-0.4153` n `13`; crypto_alt avg `-1.5295` n `239`; crypto_major avg `-1.5357` n `8`; equity avg `-1.9583` n `158`; fx avg `-0.0788` n `6`; index avg `-0.2618` n `27`; metal avg `-0.3012` n `20`; unknown avg `0.998` n `1205`
- 24h: commodity avg `-0.3422` n `13`; crypto_alt avg `-3.1977` n `239`; crypto_major avg `-3.7905` n `8`; equity avg `-1.2132` n `158`; fx avg `-0.1736` n `6`; index avg `-0.1568` n `27`; metal avg `0.1765` n `20`; unknown avg `0.995` n `982`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
