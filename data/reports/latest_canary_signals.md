# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T16:52:45.362075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0234` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4068` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1705` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0696` n `13`; crypto_alt avg `0.0967` n `239`; crypto_major avg `0.2378` n `8`; equity avg `-0.4658` n `160`; fx avg `0.0066` n `6`; index avg `-0.0375` n `27`; metal avg `0.0143` n `20`; unknown avg `2.4968` n `1262`
- 1h: commodity avg `0.4222` n `13`; crypto_alt avg `-0.4949` n `239`; crypto_major avg `-0.2635` n `8`; equity avg `-0.5847` n `160`; fx avg `-0.0218` n `6`; index avg `-0.0364` n `27`; metal avg `-0.1407` n `20`; unknown avg `3.4846` n `1250`
- 4h: commodity avg `0.5037` n `13`; crypto_alt avg `-1.4957` n `239`; crypto_major avg `-2.5197` n `8`; equity avg `-1.0777` n `160`; fx avg `-0.0902` n `6`; index avg `-0.1129` n `27`; metal avg `-0.3492` n `20`; unknown avg `21.4152` n `1250`
- 24h: commodity avg `-0.2013` n `13`; crypto_alt avg `-2.2179` n `239`; crypto_major avg `-3.8302` n `8`; equity avg `-2.1004` n `160`; fx avg `-0.1282` n `6`; index avg `-0.152` n `27`; metal avg `-0.4826` n `20`; unknown avg `3.9992` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.237`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1593`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
