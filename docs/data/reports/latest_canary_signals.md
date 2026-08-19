# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T22:46:16.990811+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.6047` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `4.3778` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `3.2778` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0995` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0088` n `12`; crypto_alt avg `-0.037` n `230`; crypto_major avg `-0.1795` n `8`; equity avg `0.0952` n `121`; fx avg `0.0182` n `6`; index avg `0.0087` n `25`; metal avg `0.0088` n `20`; unknown avg `-0.0106` n `792`
- 1h: commodity avg `-0.0687` n `12`; crypto_alt avg `-0.8552` n `230`; crypto_major avg `-1.0618` n `8`; equity avg `0.1976` n `121`; fx avg `0.0098` n `6`; index avg `0.0377` n `25`; metal avg `-0.0475` n `20`; unknown avg `0.0793` n `792`
- 4h: commodity avg `-0.048` n `12`; crypto_alt avg `2.029` n `230`; crypto_major avg `4.5567` n `8`; equity avg `1.2789` n `121`; fx avg `-0.0094` n `6`; index avg `0.1079` n `25`; metal avg `0.1789` n `20`; unknown avg `1.2116` n `792`
- 24h: commodity avg `-0.1194` n `12`; crypto_alt avg `5.3486` n `230`; crypto_major avg `10.0338` n `8`; equity avg `1.1341` n `120`; fx avg `-0.2015` n `6`; index avg `0.1688` n `25`; metal avg `1.253` n `20`; unknown avg `1.4971` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1578`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
