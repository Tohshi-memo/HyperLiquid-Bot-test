# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T22:22:23.980957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.8963` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.5738` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.1955` n `12`; crypto_alt avg `2.0352` n `228`; crypto_major avg `1.8341` n `8`; equity avg `0.5011` n `74`; fx avg `0.0088` n `6`; index avg `0.2227` n `23`; metal avg `0.1635` n `18`; unknown avg `0.4977` n `516`
- 1h: commodity avg `-0.0193` n `12`; crypto_alt avg `2.1764` n `228`; crypto_major avg `1.9135` n `8`; equity avg `0.3397` n `74`; fx avg `-0.0237` n `6`; index avg `-0.0636` n `23`; metal avg `0.0172` n `18`; unknown avg `0.3566` n `516`
- 4h: commodity avg `0.07` n `12`; crypto_alt avg `1.0747` n `228`; crypto_major avg `1.1374` n `8`; equity avg `-0.0073` n `74`; fx avg `-0.0229` n `6`; index avg `0.0079` n `23`; metal avg `-0.2798` n `18`; unknown avg `0.1982` n `516`
- 24h: commodity avg `0.2211` n `12`; crypto_alt avg `3.9847` n `228`; crypto_major avg `5.2187` n `8`; equity avg `1.6414` n `74`; fx avg `-0.0676` n `6`; index avg `0.2709` n `23`; metal avg `0.3177` n `18`; unknown avg `-4.5802` n `505`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
