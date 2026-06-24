# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T19:07:31.032574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2254` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.955` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6086` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.2171` n `228`; crypto_major avg `0.2109` n `8`; equity avg `-0.1576` n `86`; fx avg `0.01` n `6`; index avg `-0.013` n `23`; metal avg `-0.0099` n `20`; unknown avg `0.3631` n `764`
- 1h: commodity avg `-0.0921` n `12`; crypto_alt avg `0.7355` n `228`; crypto_major avg `0.5804` n `8`; equity avg `-0.3483` n `86`; fx avg `0.014` n `6`; index avg `-0.0374` n `23`; metal avg `0.0504` n `20`; unknown avg `0.557` n `764`
- 4h: commodity avg `0.0303` n `12`; crypto_alt avg `-2.5246` n `228`; crypto_major avg `-2.1951` n `8`; equity avg `-1.8019` n `86`; fx avg `0.0418` n `6`; index avg `-0.2401` n `23`; metal avg `-0.5865` n `20`; unknown avg `-0.7292` n `764`
- 24h: commodity avg `-0.5993` n `12`; crypto_alt avg `-4.0859` n `228`; crypto_major avg `-3.7677` n `8`; equity avg `1.5301` n `86`; fx avg `0.0804` n `6`; index avg `-0.0792` n `23`; metal avg `-2.0742` n `20`; unknown avg `-0.3772` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
