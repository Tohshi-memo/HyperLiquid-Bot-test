# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T17:22:32.326855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4858` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.3716` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.3338` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-2.1468` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0166` n `12`; crypto_alt avg `-0.4476` n `234`; crypto_major avg `-0.3082` n `8`; equity avg `-0.0064` n `142`; fx avg `-0.0` n `6`; index avg `0.0073` n `26`; metal avg `0.0362` n `20`; unknown avg `0.0141` n `962`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `-1.2471` n `234`; crypto_major avg `-0.8518` n `8`; equity avg `-0.2087` n `142`; fx avg `-0.0053` n `6`; index avg `-0.0291` n `26`; metal avg `0.0033` n `20`; unknown avg `9.2545` n `960`
- 4h: commodity avg `0.0436` n `12`; crypto_alt avg `-2.4249` n `234`; crypto_major avg `-2.4422` n `8`; equity avg `-0.2954` n `142`; fx avg `-0.0519` n `6`; index avg `-0.1084` n `26`; metal avg `-0.0706` n `20`; unknown avg `235.6711` n `892`
- 24h: commodity avg `-0.3883` n `12`; crypto_alt avg `-0.7052` n `234`; crypto_major avg `-1.7975` n `8`; equity avg `0.1238` n `142`; fx avg `-0.1731` n `6`; index avg `-0.0744` n `26`; metal avg `-0.2274` n `20`; unknown avg `-0.0764` n `786`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1893`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
