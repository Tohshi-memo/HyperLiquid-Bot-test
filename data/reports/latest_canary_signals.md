# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T22:52:30.216084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1784` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.1039` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0499` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.6485` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.1394` n `233`; crypto_major avg `-0.1973` n `8`; equity avg `0.0017` n `134`; fx avg `0.0001` n `6`; index avg `0.0017` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.2275` n `797`
- 1h: commodity avg `0.0253` n `12`; crypto_alt avg `-1.2094` n `233`; crypto_major avg `-0.7163` n `8`; equity avg `-0.0901` n `134`; fx avg `-0.017` n `6`; index avg `0.006` n `26`; metal avg `0.016` n `20`; unknown avg `-0.1271` n `741`
- 4h: commodity avg `0.0673` n `12`; crypto_alt avg `-3.3158` n `233`; crypto_major avg `-2.1111` n `8`; equity avg `-0.4626` n `134`; fx avg `-0.0219` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0612` n `20`; unknown avg `21.2404` n `691`
- 24h: commodity avg `0.156` n `12`; crypto_alt avg `-3.6456` n `233`; crypto_major avg `-2.3439` n `8`; equity avg `-0.6548` n `134`; fx avg `-0.027` n `6`; index avg `-0.1248` n `26`; metal avg `0.5561` n `20`; unknown avg `0.7121` n `665`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
