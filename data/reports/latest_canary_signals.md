# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T07:37:26.718662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `12`; crypto_alt avg `-0.1317` n `228`; crypto_major avg `-0.2132` n `8`; equity avg `-0.0955` n `86`; fx avg `-0.0032` n `6`; index avg `-0.027` n `23`; metal avg `-0.0961` n `20`; unknown avg `-0.0587` n `764`
- 1h: commodity avg `-0.0224` n `12`; crypto_alt avg `-0.2481` n `228`; crypto_major avg `-0.4887` n `8`; equity avg `-0.2703` n `86`; fx avg `-0.0044` n `6`; index avg `-0.035` n `23`; metal avg `-0.1858` n `20`; unknown avg `-0.194` n `756`
- 4h: commodity avg `0.036` n `12`; crypto_alt avg `-0.2544` n `228`; crypto_major avg `-0.104` n `8`; equity avg `0.2373` n `86`; fx avg `0.076` n `6`; index avg `0.1001` n `23`; metal avg `0.1187` n `20`; unknown avg `-0.0264` n `732`
- 24h: commodity avg `-0.3462` n `12`; crypto_alt avg `-0.9577` n `228`; crypto_major avg `-1.3237` n `8`; equity avg `4.3388` n `86`; fx avg `-0.044` n `6`; index avg `0.0007` n `23`; metal avg `-0.3505` n `20`; unknown avg `0.0263` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
