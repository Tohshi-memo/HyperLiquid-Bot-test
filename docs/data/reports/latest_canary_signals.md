# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T19:07:27.937180+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2252` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7304` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6974` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.3198` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.013` n `13`; crypto_alt avg `0.0494` n `235`; crypto_major avg `0.158` n `8`; equity avg `-0.0116` n `143`; fx avg `-0.0051` n `6`; index avg `0.0029` n `26`; metal avg `0.0269` n `20`; unknown avg `0.4304` n `982`
- 1h: commodity avg `-0.0867` n `13`; crypto_alt avg `-2.2777` n `235`; crypto_major avg `-1.3299` n `8`; equity avg `-0.0474` n `143`; fx avg `-0.0081` n `6`; index avg `-0.0101` n `26`; metal avg `0.0725` n `20`; unknown avg `7.2422` n `982`
- 4h: commodity avg `0.4766` n `13`; crypto_alt avg `-3.1477` n `235`; crypto_major avg `-1.7486` n `8`; equity avg `-0.368` n `143`; fx avg `-0.016` n `6`; index avg `-0.0512` n `26`; metal avg `-0.0182` n `20`; unknown avg `3.1002` n `976`
- 24h: commodity avg `-0.1921` n `13`; crypto_alt avg `-1.9599` n `235`; crypto_major avg `-1.2121` n `8`; equity avg `0.6179` n `142`; fx avg `-0.1243` n `6`; index avg `0.2741` n `26`; metal avg `-0.2157` n `20`; unknown avg `99.4595` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
