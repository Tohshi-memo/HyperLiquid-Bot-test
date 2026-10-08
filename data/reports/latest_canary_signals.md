# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T16:37:28.248679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.7313` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.6022` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.3778` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.1171` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0213` n `13`; crypto_alt avg `-0.2395` n `235`; crypto_major avg `-0.1861` n `8`; equity avg `-0.0656` n `150`; fx avg `-0.0172` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0231` n `20`; unknown avg `-0.2576` n `1077`
- 1h: commodity avg `-0.2884` n `13`; crypto_alt avg `0.524` n `235`; crypto_major avg `0.2602` n `8`; equity avg `0.2363` n `150`; fx avg `-0.0508` n `6`; index avg `0.0589` n `26`; metal avg `-0.0008` n `20`; unknown avg `1.9071` n `1069`
- 4h: commodity avg `-0.3568` n `13`; crypto_alt avg `-3.4786` n `235`; crypto_major avg `-2.7346` n `8`; equity avg `-0.6175` n `150`; fx avg `-0.02` n `6`; index avg `-0.0033` n `26`; metal avg `-0.1324` n `20`; unknown avg `0.5821` n `1021`
- 24h: commodity avg `0.5873` n `13`; crypto_alt avg `-3.5792` n `235`; crypto_major avg `-4.7251` n `8`; equity avg `-1.8775` n `150`; fx avg `0.0357` n `6`; index avg `-0.2098` n `26`; metal avg `-0.1865` n `20`; unknown avg `22.3426` n `990`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1717`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
