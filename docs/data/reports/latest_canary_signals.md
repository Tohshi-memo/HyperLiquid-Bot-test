# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T01:52:33.963268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0687` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.8279` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7675` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0493` n `12`; crypto_alt avg `-0.102` n `230`; crypto_major avg `-0.0642` n `8`; equity avg `-0.2641` n `102`; fx avg `-0.0103` n `6`; index avg `-0.0256` n `25`; metal avg `-0.0725` n `20`; unknown avg `-0.1663` n `774`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.4686` n `230`; crypto_major avg `-0.2621` n `8`; equity avg `-0.403` n `102`; fx avg `0.0088` n `6`; index avg `-0.0317` n `25`; metal avg `-0.1698` n `20`; unknown avg `0.2775` n `774`
- 4h: commodity avg `-0.0605` n `12`; crypto_alt avg `-2.4334` n `230`; crypto_major avg `-2.1292` n `8`; equity avg `-1.6515` n `102`; fx avg `0.0654` n `6`; index avg `-0.3013` n `25`; metal avg `-0.3617` n `20`; unknown avg `2.1483` n `774`
- 24h: commodity avg `-0.751` n `12`; crypto_alt avg `-4.1607` n `230`; crypto_major avg `-3.2585` n `8`; equity avg `-2.5287` n `102`; fx avg `-0.0757` n `6`; index avg `-0.5948` n `25`; metal avg `-0.4487` n `20`; unknown avg `1161.8277` n `757`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.3447`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2961`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1928`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
