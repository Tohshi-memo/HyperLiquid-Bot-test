# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T18:37:36.749974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.0889` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.9236` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.7648` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0921` n `13`; crypto_alt avg `0.1823` n `235`; crypto_major avg `0.0357` n `8`; equity avg `-0.1406` n `150`; fx avg `-0.0029` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0059` n `20`; unknown avg `2.626` n `1077`
- 1h: commodity avg `0.2323` n `13`; crypto_alt avg `1.2991` n `235`; crypto_major avg `0.9491` n `8`; equity avg `0.4006` n `150`; fx avg `0.0115` n `6`; index avg `0.0593` n `26`; metal avg `-0.0297` n `20`; unknown avg `4.685` n `1075`
- 4h: commodity avg `0.0829` n `13`; crypto_alt avg `-4.0689` n `235`; crypto_major avg `-3.006` n `8`; equity avg `-1.7461` n `150`; fx avg `-0.0493` n `6`; index avg `-0.2412` n `26`; metal avg `-0.0824` n `20`; unknown avg `1.2979` n `1069`
- 24h: commodity avg `1.027` n `13`; crypto_alt avg `-3.5493` n `235`; crypto_major avg `-4.4251` n `8`; equity avg `-3.0264` n `150`; fx avg `0.0634` n `6`; index avg `-0.4094` n `26`; metal avg `-0.0926` n `20`; unknown avg `23.2698` n `991`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1709`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1563`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1419`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
