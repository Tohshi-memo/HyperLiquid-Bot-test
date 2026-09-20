# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T10:52:30.030190+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.0451` n `234`; crypto_major avg `0.0218` n `8`; equity avg `0.0091` n `140`; fx avg `0.0015` n `6`; index avg `-0.0031` n `26`; metal avg `0.0038` n `20`; unknown avg `0.1648` n `943`
- 1h: commodity avg `0.0265` n `12`; crypto_alt avg `-0.637` n `234`; crypto_major avg `-0.2844` n `8`; equity avg `-0.0302` n `140`; fx avg `0.0066` n `6`; index avg `-0.0007` n `26`; metal avg `-0.0221` n `20`; unknown avg `0.7908` n `941`
- 4h: commodity avg `0.016` n `12`; crypto_alt avg `-0.8497` n `234`; crypto_major avg `-0.2189` n `8`; equity avg `-0.0332` n `140`; fx avg `0.0156` n `6`; index avg `-0.0029` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.3291` n `935`
- 24h: commodity avg `0.2479` n `12`; crypto_alt avg `-2.2563` n `234`; crypto_major avg `-2.0754` n `8`; equity avg `-0.2674` n `140`; fx avg `-0.0703` n `6`; index avg `-0.051` n `26`; metal avg `-0.0139` n `20`; unknown avg `0.5793` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
