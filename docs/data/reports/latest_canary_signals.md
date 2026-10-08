# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T18:22:43.520116+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1111` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.1032` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.9735` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6531` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0819` n `13`; crypto_alt avg `1.4526` n `235`; crypto_major avg `1.2027` n `8`; equity avg `0.4315` n `150`; fx avg `0.0059` n `6`; index avg `0.0617` n `26`; metal avg `-0.0224` n `20`; unknown avg `4.103` n `1077`
- 1h: commodity avg `0.423` n `13`; crypto_alt avg `1.0995` n `235`; crypto_major avg `0.9884` n `8`; equity avg `0.567` n `150`; fx avg `0.0136` n `6`; index avg `0.0565` n `26`; metal avg `-0.0736` n `20`; unknown avg `3.2139` n `1075`
- 4h: commodity avg `-0.0859` n `13`; crypto_alt avg `-4.6024` n `235`; crypto_major avg `-3.197` n `8`; equity avg `-1.5439` n `150`; fx avg `-0.0186` n `6`; index avg `-0.2235` n `26`; metal avg `-0.0938` n `20`; unknown avg `0.9267` n `1045`
- 24h: commodity avg `1.1225` n `13`; crypto_alt avg `-3.7184` n `235`; crypto_major avg `-4.3044` n `8`; equity avg `-2.9069` n `150`; fx avg `0.0656` n `6`; index avg `-0.3973` n `26`; metal avg `-0.1039` n `20`; unknown avg `23.1858` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1583`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1488`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1441`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
