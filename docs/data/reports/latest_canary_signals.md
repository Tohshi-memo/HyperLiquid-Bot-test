# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T00:22:24.514440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1463` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.5803` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5102` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `0.3345` n `230`; crypto_major avg `0.1736` n `8`; equity avg `0.0276` n `92`; fx avg `-0.0014` n `6`; index avg `-0.0057` n `25`; metal avg `-0.0075` n `20`; unknown avg `0.1223` n `765`
- 1h: commodity avg `0.1879` n `12`; crypto_alt avg `-0.4504` n `230`; crypto_major avg `-0.6317` n `8`; equity avg `-0.0765` n `92`; fx avg `-0.0007` n `6`; index avg `-0.0276` n `25`; metal avg `-0.0197` n `20`; unknown avg `0.1585` n `765`
- 4h: commodity avg `0.5377` n `12`; crypto_alt avg `-1.8869` n `230`; crypto_major avg `-1.6086` n `8`; equity avg `-0.2556` n `92`; fx avg `0.0157` n `6`; index avg `-0.0984` n `25`; metal avg `-0.0283` n `20`; unknown avg `0.9513` n `765`
- 24h: commodity avg `0.5152` n `12`; crypto_alt avg `-0.8016` n `229`; crypto_major avg `-0.7149` n `8`; equity avg `0.0603` n `92`; fx avg `0.0203` n `6`; index avg `-0.0593` n `25`; metal avg `-0.0595` n `20`; unknown avg `0.7429` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
