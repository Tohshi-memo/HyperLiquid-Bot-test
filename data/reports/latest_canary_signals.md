# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T17:22:29.083477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-4.1147` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `3.8056` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.7785` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-1.8583` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_index_leads_crypto: score `1.0468` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0124` n `13`; crypto_alt avg `-0.4186` n `235`; crypto_major avg `-0.3762` n `8`; equity avg `-0.1153` n `150`; fx avg `0.0134` n `6`; index avg `0.0061` n `26`; metal avg `0.0366` n `20`; unknown avg `0.0467` n `1077`
- 1h: commodity avg `-0.0664` n `13`; crypto_alt avg `-1.6024` n `235`; crypto_major avg `-1.2681` n `8`; equity avg `-1.5147` n `150`; fx avg `-0.0069` n `6`; index avg `-0.2213` n `26`; metal avg `0.1142` n `20`; unknown avg `0.1432` n `1075`
- 4h: commodity avg `-0.2945` n `13`; crypto_alt avg `-4.9404` n `235`; crypto_major avg `-4.073` n `8`; equity avg `-2.2147` n `150`; fx avg `0.0083` n `6`; index avg `-0.2674` n `26`; metal avg `0.0417` n `20`; unknown avg `1.0702` n `1021`
- 24h: commodity avg `0.7607` n `13`; crypto_alt avg `-4.7505` n `235`; crypto_major avg `-5.5987` n `8`; equity avg `-3.4818` n `150`; fx avg `0.058` n `6`; index avg `-0.4713` n `26`; metal avg `-0.1181` n `20`; unknown avg `23.8041` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1439`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
