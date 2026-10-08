# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T15:37:47.577874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-3.2757` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.2299` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-3.2278` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-3.1458` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `3.0505` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-3.0464` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.5058` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-2.2377` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `-1.6571` n `235`; crypto_major avg `-1.2194` n `8`; equity avg `-0.3054` n `150`; fx avg `0.0001` n `6`; index avg `-0.0246` n `26`; metal avg `-0.0116` n `20`; unknown avg `2.4166` n `1077`
- 1h: commodity avg `0.0903` n `13`; crypto_alt avg `-4.4526` n `235`; crypto_major avg `-3.1854` n `8`; equity avg `-0.9477` n `150`; fx avg `-0.0191` n `6`; index avg `-0.1349` n `26`; metal avg `-0.139` n `20`; unknown avg `1.9652` n `1075`
- 4h: commodity avg `-0.042` n `13`; crypto_alt avg `-4.2551` n `235`; crypto_major avg `-3.2698` n `8`; equity avg `-0.764` n `150`; fx avg `0.0476` n `6`; index avg `-0.0399` n `26`; metal avg `-0.124` n `20`; unknown avg `0.353` n `1021`
- 24h: commodity avg `0.6904` n `13`; crypto_alt avg `-3.5166` n `235`; crypto_major avg `-4.8592` n `8`; equity avg `-2.1393` n `150`; fx avg `0.0869` n `6`; index avg `-0.2583` n `26`; metal avg `-0.2012` n `20`; unknown avg `23.3595` n `990`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1577`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
