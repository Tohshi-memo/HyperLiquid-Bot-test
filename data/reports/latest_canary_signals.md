# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T15:37:31.959289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0` n `12`; crypto_alt avg `0.1382` n `229`; crypto_major avg `0.144` n `8`; equity avg `-0.004` n `88`; fx avg `0.0221` n `6`; index avg `-0.0069` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0328` n `747`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.2774` n `229`; crypto_major avg `0.3005` n `8`; equity avg `0.0308` n `88`; fx avg `-0.0005` n `6`; index avg `-0.0121` n `25`; metal avg `0.0152` n `20`; unknown avg `0.1313` n `747`
- 4h: commodity avg `-0.0135` n `12`; crypto_alt avg `0.6238` n `229`; crypto_major avg `0.8395` n `8`; equity avg `-0.0176` n `88`; fx avg `-0.0695` n `6`; index avg `0.041` n `25`; metal avg `0.0261` n `20`; unknown avg `0.2716` n `747`
- 24h: commodity avg `-0.0076` n `12`; crypto_alt avg `-1.3372` n `229`; crypto_major avg `-0.7888` n `8`; equity avg `0.2613` n `88`; fx avg `-0.0819` n `6`; index avg `0.0714` n `25`; metal avg `0.0857` n `20`; unknown avg `-0.5472` n `713`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
