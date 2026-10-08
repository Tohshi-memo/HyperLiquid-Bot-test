# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T16:22:27.609470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.7001` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.5731` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-2.3141` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_equity_divergence: score `-2.1979` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.3005` n `13`; crypto_alt avg `0.8857` n `235`; crypto_major avg `0.4063` n `8`; equity avg `0.2805` n `150`; fx avg `-0.0147` n `6`; index avg `0.0691` n `26`; metal avg `0.1159` n `20`; unknown avg `2.2048` n `1077`
- 1h: commodity avg `-0.2575` n `13`; crypto_alt avg `-0.9098` n `235`; crypto_major avg `-0.7783` n `8`; equity avg `-0.0054` n `150`; fx avg `-0.0336` n `6`; index avg `0.0418` n `26`; metal avg `0.0108` n `20`; unknown avg `1.0579` n `1069`
- 4h: commodity avg `-0.3888` n `13`; crypto_alt avg `-3.4228` n `235`; crypto_major avg `-2.7029` n `8`; equity avg `-0.505` n `150`; fx avg `-0.0054` n `6`; index avg `-0.0028` n `26`; metal avg `-0.1298` n `20`; unknown avg `0.7555` n `1021`
- 24h: commodity avg `0.6479` n `13`; crypto_alt avg `-3.451` n `235`; crypto_major avg `-4.7222` n `8`; equity avg `-1.9016` n `150`; fx avg `0.0492` n `6`; index avg `-0.2185` n `26`; metal avg `-0.1866` n `20`; unknown avg `22.458` n `990`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
