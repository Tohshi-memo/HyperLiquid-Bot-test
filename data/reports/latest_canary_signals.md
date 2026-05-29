# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T20:22:21.145826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0258` n `12`; crypto_alt avg `0.1132` n `228`; crypto_major avg `0.0665` n `8`; equity avg `-0.0922` n `69`; fx avg `0.0061` n `6`; index avg `-0.0057` n `23`; metal avg `0.0102` n `18`; unknown avg `-0.2031` n `419`
- 1h: commodity avg `0.1159` n `12`; crypto_alt avg `0.6778` n `228`; crypto_major avg `0.5164` n `8`; equity avg `0.4033` n `69`; fx avg `0.0274` n `6`; index avg `0.1152` n `23`; metal avg `-0.1543` n `18`; unknown avg `0.0177` n `419`
- 4h: commodity avg `-0.0485` n `12`; crypto_alt avg `-0.2484` n `228`; crypto_major avg `-0.0286` n `8`; equity avg `0.0067` n `69`; fx avg `0.0412` n `6`; index avg `0.0873` n `23`; metal avg `-0.1435` n `18`; unknown avg `-0.2825` n `419`
- 24h: commodity avg `-0.7061` n `12`; crypto_alt avg `0.6956` n `228`; crypto_major avg `1.1565` n `8`; equity avg `1.3293` n `69`; fx avg `0.2367` n `6`; index avg `0.1589` n `23`; metal avg `0.1395` n `18`; unknown avg `0.5746` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.159`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
