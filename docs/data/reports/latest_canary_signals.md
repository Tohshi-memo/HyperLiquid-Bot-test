# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T18:07:28.337447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.29` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-2.4525` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `2.4121` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.3444` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0941` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.094` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.6216` n `233`; crypto_major avg `-0.7145` n `8`; equity avg `-0.1486` n `136`; fx avg `-0.0018` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0297` n `20`; unknown avg `9.3172` n `804`
- 1h: commodity avg `-0.0528` n `12`; crypto_alt avg `-1.2134` n `233`; crypto_major avg `-1.0815` n `8`; equity avg `-0.0295` n `136`; fx avg `-0.0059` n `6`; index avg `0.0125` n `26`; metal avg `-0.021` n `20`; unknown avg `9.4557` n `758`
- 4h: commodity avg `0.0145` n `12`; crypto_alt avg `-1.6697` n `233`; crypto_major avg `-2.3299` n `8`; equity avg `0.1226` n `136`; fx avg `0.021` n `6`; index avg `0.0822` n `26`; metal avg `-0.2358` n `20`; unknown avg `4.2271` n `752`
- 24h: commodity avg `-0.5596` n `12`; crypto_alt avg `0.3937` n `233`; crypto_major avg `1.0758` n `8`; equity avg `0.569` n `136`; fx avg `-0.1524` n `6`; index avg `0.3482` n `26`; metal avg `0.1615` n `20`; unknown avg `5.0339` n `666`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
