# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T06:22:26.050113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.4095` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.3357` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0878` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.5578` n `228`; crypto_major avg `0.7093` n `8`; equity avg `0.2561` n `86`; fx avg `-0.0919` n `6`; index avg `0.0681` n `23`; metal avg `0.2713` n `20`; unknown avg `6.5654` n `757`
- 1h: commodity avg `0.159` n `12`; crypto_alt avg `0.5267` n `228`; crypto_major avg `0.7293` n `8`; equity avg `0.1855` n `86`; fx avg `-0.0999` n `6`; index avg `0.0456` n `23`; metal avg `0.3111` n `20`; unknown avg `0.0127` n `741`
- 4h: commodity avg `0.0328` n `12`; crypto_alt avg `2.1219` n `228`; crypto_major avg `2.3685` n `8`; equity avg `-0.041` n `86`; fx avg `-0.1115` n `6`; index avg `-0.0581` n `23`; metal avg `0.2807` n `20`; unknown avg `0.4896` n `725`
- 24h: commodity avg `0.4095` n `12`; crypto_alt avg `-2.409` n `228`; crypto_major avg `-2.3884` n `8`; equity avg `-4.0705` n `86`; fx avg `-0.0466` n `6`; index avg `-0.6479` n `23`; metal avg `0.4228` n `20`; unknown avg `0.8031` n `693`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
