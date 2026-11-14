# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T22:07:25.747978+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `3.9572` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.9516` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.6473` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-3.4082` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.6607` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `-1.5597` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.4898` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0092` n `13`; crypto_alt avg `-0.3644` n `239`; crypto_major avg `-0.5009` n `8`; equity avg `-0.1418` n `162`; fx avg `-0.0071` n `6`; index avg `0.0016` n `27`; metal avg `0.0142` n `20`; unknown avg `0.2365` n `1250`
- 1h: commodity avg `0.0034` n `13`; crypto_alt avg `-0.6762` n `239`; crypto_major avg `-1.4658` n `8`; equity avg `0.1949` n `162`; fx avg `0.0086` n `6`; index avg `0.024` n `27`; metal avg `0.0939` n `20`; unknown avg `200.5828` n `1254`
- 4h: commodity avg `-0.0226` n `13`; crypto_alt avg `-3.791` n `239`; crypto_major avg `-3.9742` n `8`; equity avg `-0.566` n `162`; fx avg `0.0078` n `6`; index avg `-0.017` n `27`; metal avg `-0.3269` n `20`; unknown avg `-0.086` n `1208`
- 24h: commodity avg `-0.0859` n `13`; crypto_alt avg `-9.3207` n `239`; crypto_major avg `-8.914` n `8`; equity avg `-1.8847` n `162`; fx avg `-0.0038` n `6`; index avg `-0.1552` n `27`; metal avg `-0.5326` n `20`; unknown avg `0.0038` n `1098`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
