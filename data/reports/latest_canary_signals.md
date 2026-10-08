# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T15:52:36.192446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7518` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.6904` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_commodity_crypto_divergence: score `-2.6249` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_index_leads_crypto: score `2.5649` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5395` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `-2.507` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `-2.0611` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_equity_divergence: score `-2.0297` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `0.8563` n `235`; crypto_major avg `0.5739` n `8`; equity avg `0.1126` n `150`; fx avg `-0.0084` n `6`; index avg `0.0078` n `26`; metal avg `-0.0601` n `20`; unknown avg `3.5162` n `1077`
- 1h: commodity avg `-0.0213` n `13`; crypto_alt avg `-3.6532` n `235`; crypto_major avg `-2.6462` n `8`; equity avg `-0.5851` n `150`; fx avg `-0.0186` n `6`; index avg `-0.0813` n `26`; metal avg `-0.1392` n `20`; unknown avg `0.966` n `1075`
- 4h: commodity avg `0.0034` n `13`; crypto_alt avg `-3.5232` n `235`; crypto_major avg `-2.7484` n `8`; equity avg `-0.7187` n `150`; fx avg `0.0388` n `6`; index avg `-0.058` n `26`; metal avg `-0.2089` n `20`; unknown avg `0.6395` n `1021`
- 24h: commodity avg `0.7544` n `13`; crypto_alt avg `-2.9984` n `235`; crypto_major avg `-4.3479` n `8`; equity avg `-2.1003` n `150`; fx avg `0.0867` n `6`; index avg `-0.2636` n `26`; metal avg `-0.2072` n `20`; unknown avg `22.3385` n `990`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1287`, n `668`, weak_sample_signal
