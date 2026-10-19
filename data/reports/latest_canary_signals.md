# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T00:37:28.959879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.0139` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.2716` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0044` n `13`; crypto_alt avg `-0.0291` n `237`; crypto_major avg `0.0355` n `8`; equity avg `-0.2255` n `151`; fx avg `0.0169` n `6`; index avg `-0.0521` n `26`; metal avg `-0.0191` n `20`; unknown avg `1.4569` n `1174`
- 1h: commodity avg `-0.053` n `13`; crypto_alt avg `0.0903` n `237`; crypto_major avg `0.028` n `8`; equity avg `0.4657` n `151`; fx avg `0.0326` n `6`; index avg `0.0891` n `26`; metal avg `-0.0062` n `20`; unknown avg `1.3801` n `1164`
- 4h: commodity avg `-0.4779` n `13`; crypto_alt avg `3.1563` n `237`; crypto_major avg `2.536` n `8`; equity avg `2.0627` n `151`; fx avg `0.0343` n `6`; index avg `0.3942` n `26`; metal avg `0.2644` n `20`; unknown avg `6.739` n `1076`
- 24h: commodity avg `-0.3542` n `13`; crypto_alt avg `-0.6542` n `237`; crypto_major avg `0.6389` n `8`; equity avg `1.762` n `151`; fx avg `0.0072` n `6`; index avg `0.3379` n `26`; metal avg `0.2024` n `20`; unknown avg `4.3072` n `939`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2034`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1373`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0879`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0825`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0591`, n `666`, weak_sample_signal
