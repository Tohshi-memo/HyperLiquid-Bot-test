# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T16:22:39.968376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4148` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `-2.1979` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0704` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.791` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.7606` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.6518` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.317` n `13`; crypto_alt avg `0.2829` n `239`; crypto_major avg `0.14` n `8`; equity avg `-0.2294` n `160`; fx avg `-0.0093` n `6`; index avg `-0.0304` n `27`; metal avg `-0.1075` n `20`; unknown avg `0.0622` n `1260`
- 1h: commodity avg `0.3072` n `13`; crypto_alt avg `-1.6741` n `239`; crypto_major avg `-1.8907` n `8`; equity avg `-1.2842` n `160`; fx avg `-0.0592` n `6`; index avg `-0.1301` n `27`; metal avg `-0.2389` n `20`; unknown avg `-0.3177` n `1250`
- 4h: commodity avg `0.2631` n `13`; crypto_alt avg `-0.8225` n `239`; crypto_major avg `-2.1517` n `8`; equity avg `-0.7575` n `160`; fx avg `-0.103` n `6`; index avg `-0.0813` n `27`; metal avg `-0.3607` n `20`; unknown avg `19.5111` n `1250`
- 24h: commodity avg `-0.2885` n `13`; crypto_alt avg `-1.6446` n `239`; crypto_major avg `-3.4393` n `8`; equity avg `-1.1341` n `160`; fx avg `-0.1242` n `6`; index avg `-0.0655` n `27`; metal avg `-0.5336` n `20`; unknown avg `0.797` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.236`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
