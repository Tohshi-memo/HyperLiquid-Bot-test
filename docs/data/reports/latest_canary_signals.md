# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T17:37:35.511383+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.14` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-2.1214` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.0561` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.0535` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0` n `12`; crypto_alt avg `0.1763` n `234`; crypto_major avg `0.1309` n `8`; equity avg `0.0647` n `142`; fx avg `-0.0029` n `6`; index avg `0.017` n `26`; metal avg `-0.0` n `20`; unknown avg `0.6575` n `962`
- 1h: commodity avg `0.0386` n `12`; crypto_alt avg `-0.9328` n `234`; crypto_major avg `-0.6598` n `8`; equity avg `-0.1417` n `142`; fx avg `-0.0112` n `6`; index avg `-0.015` n `26`; metal avg `-0.0343` n `20`; unknown avg `11.3037` n `960`
- 4h: commodity avg `0.0287` n `12`; crypto_alt avg `-2.0541` n `234`; crypto_major avg `-2.0927` n `8`; equity avg `0.0473` n `142`; fx avg `-0.065` n `6`; index avg `-0.0366` n `26`; metal avg `-0.0392` n `20`; unknown avg `229.5461` n `892`
- 24h: commodity avg `-0.4544` n `12`; crypto_alt avg `-0.4203` n `234`; crypto_major avg `-1.4218` n `8`; equity avg `0.3091` n `142`; fx avg `-0.1853` n `6`; index avg `-0.0521` n `26`; metal avg `-0.2238` n `20`; unknown avg `0.0743` n `786`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1911`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1422`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
