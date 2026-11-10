# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T19:07:32.760429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.106` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.6284` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5935` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.2662` n `239`; crypto_major avg `-0.1252` n `8`; equity avg `0.1449` n `160`; fx avg `0.0009` n `6`; index avg `0.0245` n `27`; metal avg `0.0151` n `20`; unknown avg `-0.307` n `1262`
- 1h: commodity avg `-0.0706` n `13`; crypto_alt avg `0.1393` n `239`; crypto_major avg `0.6053` n `8`; equity avg `0.4964` n `160`; fx avg `0.0141` n `6`; index avg `0.0581` n `27`; metal avg `0.0789` n `20`; unknown avg `-0.2484` n `1256`
- 4h: commodity avg `0.3038` n `13`; crypto_alt avg `-2.2773` n `239`; crypto_major avg `-1.8022` n `8`; equity avg `-2.0659` n `160`; fx avg `-0.0437` n `6`; index avg `-0.2087` n `27`; metal avg `-0.1738` n `20`; unknown avg `-0.6142` n `1250`
- 24h: commodity avg `-0.2827` n `13`; crypto_alt avg `-1.8388` n `239`; crypto_major avg `-2.7455` n `8`; equity avg `-1.5396` n `160`; fx avg `-0.0974` n `6`; index avg `-0.1603` n `27`; metal avg `-0.4475` n `20`; unknown avg `0.004` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2464`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1775`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
