# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T16:52:38.716199+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.8193` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.7322` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.5159` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.002` n `13`; crypto_alt avg `-0.4443` n `235`; crypto_major avg `-0.2903` n `8`; equity avg `-1.0096` n `150`; fx avg `0.0124` n `6`; index avg `-0.1477` n `26`; metal avg `0.0074` n `20`; unknown avg `1.266` n `1077`
- 1h: commodity avg `-0.2918` n `13`; crypto_alt avg `-0.7714` n `235`; crypto_major avg `-0.6003` n `8`; equity avg `-0.8896` n `150`; fx avg `-0.03` n `6`; index avg `-0.0969` n `26`; metal avg `0.0669` n `20`; unknown avg `1.1397` n `1069`
- 4h: commodity avg `-0.3545` n `13`; crypto_alt avg `-3.5645` n `235`; crypto_major avg `-2.8704` n `8`; equity avg `-1.507` n `150`; fx avg `-0.005` n `6`; index avg `-0.1382` n `26`; metal avg `-0.0511` n `20`; unknown avg `1.0567` n `1021`
- 24h: commodity avg `0.5885` n `13`; crypto_alt avg `-4.0031` n `235`; crypto_major avg `-4.9993` n `8`; equity avg `-2.8557` n `150`; fx avg `0.0481` n `6`; index avg `-0.3558` n `26`; metal avg `-0.179` n `20`; unknown avg `24.0041` n `990`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1752`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.159`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
