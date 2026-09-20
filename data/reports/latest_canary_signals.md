# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T16:37:26.645652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.8065` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5097` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0365` n `12`; crypto_alt avg `0.7422` n `234`; crypto_major avg `0.6273` n `8`; equity avg `0.0585` n `140`; fx avg `0.0018` n `6`; index avg `0.005` n `26`; metal avg `0.0069` n `20`; unknown avg `2.1275` n `943`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `1.7481` n `234`; crypto_major avg `1.3045` n `8`; equity avg `0.2563` n `140`; fx avg `0.0205` n `6`; index avg `0.0303` n `26`; metal avg `0.0193` n `20`; unknown avg `0.5812` n `889`
- 4h: commodity avg `0.0219` n `12`; crypto_alt avg `2.3462` n `234`; crypto_major avg `1.8297` n `8`; equity avg `0.32` n `140`; fx avg `0.0204` n `6`; index avg `0.0371` n `26`; metal avg `0.0232` n `20`; unknown avg `1.4265` n `889`
- 24h: commodity avg `0.4636` n `12`; crypto_alt avg `-0.3305` n `234`; crypto_major avg `-0.9034` n `8`; equity avg `-0.008` n `140`; fx avg `-0.0223` n `6`; index avg `-0.0322` n `26`; metal avg `0.0001` n `20`; unknown avg `154.7382` n `795`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
