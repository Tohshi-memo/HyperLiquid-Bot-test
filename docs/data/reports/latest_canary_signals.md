# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T18:52:33.780775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.8754` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.5159` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.1416` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0547` n `12`; crypto_alt avg `-0.3992` n `228`; crypto_major avg `-0.3389` n `8`; equity avg `-0.487` n `86`; fx avg `-0.0088` n `6`; index avg `-0.0725` n `23`; metal avg `-0.1091` n `20`; unknown avg `0.0034` n `764`
- 1h: commodity avg `-0.1185` n `12`; crypto_alt avg `0.8045` n `228`; crypto_major avg `0.6334` n `8`; equity avg `-0.1244` n `86`; fx avg `-0.0003` n `6`; index avg `-0.0264` n `23`; metal avg `-0.0937` n `20`; unknown avg `0.2656` n `764`
- 4h: commodity avg `0.0893` n `12`; crypto_alt avg `-3.1123` n `228`; crypto_major avg `-2.7861` n `8`; equity avg `-1.7175` n `86`; fx avg `0.0613` n `6`; index avg `-0.2702` n `23`; metal avg `-0.6445` n `20`; unknown avg `-0.7636` n `764`
- 24h: commodity avg `-0.6004` n `12`; crypto_alt avg `-4.1123` n `228`; crypto_major avg `-3.8587` n `8`; equity avg `1.8947` n `86`; fx avg `0.0669` n `6`; index avg `0.0015` n `23`; metal avg `-1.9635` n `20`; unknown avg `-0.4522` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
