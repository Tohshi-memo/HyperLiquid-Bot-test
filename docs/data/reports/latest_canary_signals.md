# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T17:07:32.078243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0887` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.9599` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.9541` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.82` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0492` n `12`; crypto_alt avg `0.0022` n `234`; crypto_major avg `0.1544` n `8`; equity avg `-0.0315` n `142`; fx avg `-0.0014` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0299` n `20`; unknown avg `0.2702` n `960`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `-0.6152` n `234`; crypto_major avg `-0.282` n `8`; equity avg `-0.2556` n `142`; fx avg `-0.0086` n `6`; index avg `-0.0406` n `26`; metal avg `-0.0144` n `20`; unknown avg `9.4627` n `960`
- 4h: commodity avg `0.021` n `12`; crypto_alt avg `-1.9066` n `234`; crypto_major avg `-2.0677` n `8`; equity avg `-0.2477` n `142`; fx avg `-0.0369` n `6`; index avg `-0.1078` n `26`; metal avg `-0.1136` n `20`; unknown avg `239.6302` n `892`
- 24h: commodity avg `-0.5633` n `12`; crypto_alt avg `0.5338` n `234`; crypto_major avg `-0.753` n `8`; equity avg `0.4659` n `142`; fx avg `-0.1862` n `6`; index avg `-0.0365` n `26`; metal avg `-0.1738` n `20`; unknown avg `2.0224` n `785`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1912`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1909`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
