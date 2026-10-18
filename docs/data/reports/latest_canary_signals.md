# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T23:37:45.793605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.798` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1808` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0581` n `13`; crypto_alt avg `0.2819` n `237`; crypto_major avg `0.3101` n `8`; equity avg `0.0752` n `151`; fx avg `0.0058` n `6`; index avg `0.0225` n `26`; metal avg `-0.0038` n `20`; unknown avg `3.6854` n `1194`
- 1h: commodity avg `-0.0505` n `13`; crypto_alt avg `0.8766` n `237`; crypto_major avg `0.6421` n `8`; equity avg `0.2719` n `151`; fx avg `-0.0172` n `6`; index avg `0.0092` n `26`; metal avg `0.0028` n `20`; unknown avg `1.1007` n `1192`
- 4h: commodity avg `-0.3824` n `13`; crypto_alt avg `2.7363` n `237`; crypto_major avg `2.4156` n `8`; equity avg `1.5792` n `151`; fx avg `-0.0201` n `6`; index avg `0.2874` n `26`; metal avg `0.2348` n `20`; unknown avg `9.6577` n `1090`
- 24h: commodity avg `-0.3482` n `13`; crypto_alt avg `-1.3526` n `236`; crypto_major avg `0.781` n `8`; equity avg `1.1505` n `151`; fx avg `-0.0215` n `6`; index avg `0.2318` n `26`; metal avg `0.2253` n `20`; unknown avg `6.8258` n `961`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2002`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1369`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0905`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0867`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `666`, weak_sample_signal
