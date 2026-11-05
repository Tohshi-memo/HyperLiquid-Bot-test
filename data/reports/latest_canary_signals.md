# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T14:37:33.398351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8294` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.401` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0922` n `13`; crypto_alt avg `-0.5328` n `239`; crypto_major avg `-0.4706` n `8`; equity avg `-1.6808` n `158`; fx avg `-0.0232` n `6`; index avg `-0.1368` n `27`; metal avg `-0.0976` n `20`; unknown avg `8.731` n `1256`
- 1h: commodity avg `0.0996` n `13`; crypto_alt avg `-0.7444` n `239`; crypto_major avg `-0.6677` n `8`; equity avg `-1.9226` n `158`; fx avg `-0.0064` n `6`; index avg `-0.1828` n `27`; metal avg `0.0942` n `20`; unknown avg `8.6417` n `1252`
- 4h: commodity avg `0.2856` n `13`; crypto_alt avg `-1.5449` n `239`; crypto_major avg `-1.6579` n `8`; equity avg `-3.0219` n `158`; fx avg `0.0129` n `6`; index avg `-0.2569` n `27`; metal avg `0.1715` n `20`; unknown avg `174.0292` n `1239`
- 24h: commodity avg `-0.5134` n `13`; crypto_alt avg `-0.6511` n `239`; crypto_major avg `-0.0426` n `8`; equity avg `-4.7466` n `158`; fx avg `-0.0323` n `6`; index avg `-0.5034` n `27`; metal avg `0.765` n `20`; unknown avg `195.6796` n `1066`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.23`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2107`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.2038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
