# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T04:51:23.247357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.3758` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.1302` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.0841` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.0137` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0253` n `13`; crypto_alt avg `-0.0568` n `239`; crypto_major avg `0.0072` n `8`; equity avg `0.187` n `162`; fx avg `0.0038` n `6`; index avg `0.0102` n `27`; metal avg `0.0177` n `20`; unknown avg `0.8246` n `1262`
- 1h: commodity avg `0.0246` n `13`; crypto_alt avg `0.0207` n `239`; crypto_major avg `-0.1694` n `8`; equity avg `0.152` n `162`; fx avg `0.009` n `6`; index avg `0.031` n `27`; metal avg `-0.0578` n `20`; unknown avg `0.2953` n `1250`
- 4h: commodity avg `-0.0649` n `13`; crypto_alt avg `-2.7278` n `239`; crypto_major avg `-3.1951` n `8`; equity avg `-1.1814` n `162`; fx avg `-0.0235` n `6`; index avg `-0.111` n `27`; metal avg `0.1807` n `20`; unknown avg `14.7508` n `1246`
- 24h: commodity avg `0.9473` n `13`; crypto_alt avg `-3.2811` n `239`; crypto_major avg `-4.6592` n `8`; equity avg `-1.0658` n `162`; fx avg `-0.0094` n `6`; index avg `0.0271` n `27`; metal avg `-0.4195` n `20`; unknown avg `99.331` n `1123`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1783`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
