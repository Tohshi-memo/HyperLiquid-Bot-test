# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T12:52:28.819448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.1162` n `228`; crypto_major avg `-0.0395` n `8`; equity avg `-0.1033` n `74`; fx avg `-0.0031` n `6`; index avg `0.0119` n `23`; metal avg `-0.0495` n `18`; unknown avg `-0.0405` n `645`
- 1h: commodity avg `0.1234` n `12`; crypto_alt avg `-0.4777` n `228`; crypto_major avg `-0.5157` n `8`; equity avg `-0.3172` n `74`; fx avg `0.016` n `6`; index avg `0.0221` n `23`; metal avg `-0.0493` n `18`; unknown avg `0.0089` n `645`
- 4h: commodity avg `0.3676` n `12`; crypto_alt avg `-0.5796` n `228`; crypto_major avg `-0.2817` n `8`; equity avg `0.0343` n `74`; fx avg `0.0233` n `6`; index avg `0.1367` n `23`; metal avg `-0.0999` n `18`; unknown avg `0.1003` n `629`
- 24h: commodity avg `-0.148` n `12`; crypto_alt avg `-0.7861` n `228`; crypto_major avg `-0.1485` n `8`; equity avg `0.621` n `74`; fx avg `0.0092` n `6`; index avg `0.2033` n `23`; metal avg `-0.0633` n `18`; unknown avg `-1.2109` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
