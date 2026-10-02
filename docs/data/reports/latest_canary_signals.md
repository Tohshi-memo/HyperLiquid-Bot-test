# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T19:56:45.429682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3268` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.0571` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.859` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7864` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1252` n `13`; crypto_alt avg `-0.2572` n `235`; crypto_major avg `-0.1082` n `8`; equity avg `-0.1592` n `143`; fx avg `-0.0062` n `6`; index avg `-0.0173` n `26`; metal avg `-0.0207` n `20`; unknown avg `3.8583` n `984`
- 1h: commodity avg `0.1764` n `13`; crypto_alt avg `-0.0759` n `235`; crypto_major avg `0.0166` n `8`; equity avg `0.092` n `143`; fx avg `-0.0016` n `6`; index avg `0.0334` n `26`; metal avg `0.08` n `20`; unknown avg `14.9167` n `982`
- 4h: commodity avg `0.4671` n `13`; crypto_alt avg `-3.5307` n `235`; crypto_major avg `-1.8597` n `8`; equity avg `-0.0733` n `143`; fx avg `0.0114` n `6`; index avg `-0.0007` n `26`; metal avg `0.1974` n `20`; unknown avg `10.7269` n `976`
- 24h: commodity avg `-0.0693` n `13`; crypto_alt avg `-2.0685` n `235`; crypto_major avg `-1.2136` n `8`; equity avg `0.6284` n `142`; fx avg `-0.1315` n `6`; index avg `0.2626` n `26`; metal avg `-0.2342` n `20`; unknown avg `103.5451` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
