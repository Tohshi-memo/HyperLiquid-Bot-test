# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T16:22:33.136917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `4.2851` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `3.5973` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.8389` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0706` n `13`; crypto_alt avg `0.1307` n `239`; crypto_major avg `0.0519` n `8`; equity avg `0.2069` n `158`; fx avg `0.0054` n `6`; index avg `0.0207` n `27`; metal avg `-0.0361` n `20`; unknown avg `-0.076` n `1264`
- 1h: commodity avg `-0.4949` n `13`; crypto_alt avg `-0.4288` n `239`; crypto_major avg `-0.2292` n `8`; equity avg `-1.614` n `158`; fx avg `-0.0171` n `6`; index avg `-0.1142` n `27`; metal avg `0.0653` n `20`; unknown avg `0.0818` n `1250`
- 4h: commodity avg `-0.7078` n `13`; crypto_alt avg `2.0544` n `239`; crypto_major avg `2.8895` n `8`; equity avg `-1.3956` n `158`; fx avg `-0.0248` n `6`; index avg `-0.018` n `27`; metal avg `0.0506` n `20`; unknown avg `0.6332` n `1250`
- 24h: commodity avg `-0.8925` n `13`; crypto_alt avg `2.9866` n `239`; crypto_major avg `3.0507` n `8`; equity avg `-1.1813` n `158`; fx avg `0.0871` n `6`; index avg `0.0484` n `27`; metal avg `0.9287` n `20`; unknown avg `0.0161` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2621`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
