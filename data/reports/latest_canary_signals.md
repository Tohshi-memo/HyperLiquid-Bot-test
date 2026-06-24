# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T21:37:29.560893+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.836` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5551` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0073` n `12`; crypto_alt avg `0.3422` n `228`; crypto_major avg `0.4034` n `8`; equity avg `0.1894` n `86`; fx avg `-0.0167` n `6`; index avg `0.0392` n `23`; metal avg `0.0211` n `20`; unknown avg `4.9712` n `764`
- 1h: commodity avg `0.0329` n `12`; crypto_alt avg `0.2821` n `228`; crypto_major avg `0.3692` n `8`; equity avg `0.2589` n `86`; fx avg `-0.0154` n `6`; index avg `0.1206` n `23`; metal avg `0.0312` n `20`; unknown avg `-0.794` n `764`
- 4h: commodity avg `-0.0485` n `12`; crypto_alt avg `2.8868` n `228`; crypto_major avg `2.7875` n `8`; equity avg `2.5445` n `86`; fx avg `-0.0102` n `6`; index avg `0.6678` n `23`; metal avg `0.2324` n `20`; unknown avg `6.1077` n `764`
- 24h: commodity avg `-0.5318` n `12`; crypto_alt avg `-2.6232` n `228`; crypto_major avg `-1.9128` n `8`; equity avg `4.1304` n `86`; fx avg `0.0435` n `6`; index avg `0.598` n `23`; metal avg `-1.6568` n `20`; unknown avg `-0.864` n `724`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
