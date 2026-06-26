# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T06:19:40.051226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.952` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.7146` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0033` n `12`; crypto_alt avg `0.075` n `228`; crypto_major avg `0.1183` n `8`; equity avg `0.1106` n `86`; fx avg `-0.0931` n `6`; index avg `0.0542` n `23`; metal avg `0.042` n `20`; unknown avg `6.3652` n `757`
- 1h: commodity avg `0.1494` n `12`; crypto_alt avg `0.044` n `228`; crypto_major avg `0.1382` n `8`; equity avg `0.0402` n `86`; fx avg `-0.1012` n `6`; index avg `0.0317` n `23`; metal avg `0.0815` n `20`; unknown avg `-0.1857` n `741`
- 4h: commodity avg `0.0232` n `12`; crypto_alt avg `1.6288` n `228`; crypto_major avg `1.7661` n `8`; equity avg `-0.1859` n `86`; fx avg `-0.1128` n `6`; index avg `-0.0719` n `23`; metal avg `0.0515` n `20`; unknown avg `0.2918` n `725`
- 24h: commodity avg `0.3998` n `12`; crypto_alt avg `-2.8729` n `228`; crypto_major avg `-2.959` n `8`; equity avg `-4.2063` n `86`; fx avg `-0.0479` n `6`; index avg `-0.6613` n `23`; metal avg `0.1934` n `20`; unknown avg `0.5966` n `693`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2158`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
