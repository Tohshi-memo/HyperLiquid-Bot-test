# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T04:37:16.541709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1355` n `12`; crypto_alt avg `-0.6238` n `228`; crypto_major avg `-0.4228` n `8`; equity avg `-0.0218` n `69`; fx avg `-0.001` n `6`; index avg `0.0235` n `23`; metal avg `-0.0016` n `18`; unknown avg `-0.3259` n `419`
- 1h: commodity avg `-0.1553` n `12`; crypto_alt avg `-1.0946` n `228`; crypto_major avg `-0.8041` n `8`; equity avg `-0.0898` n `69`; fx avg `-0.0029` n `6`; index avg `0.0327` n `23`; metal avg `-0.0639` n `18`; unknown avg `0.487` n `419`
- 4h: commodity avg `-0.2845` n `12`; crypto_alt avg `-0.2347` n `228`; crypto_major avg `-0.0092` n `8`; equity avg `0.1695` n `69`; fx avg `0.0` n `6`; index avg `-0.0408` n `23`; metal avg `-0.0422` n `18`; unknown avg `-0.5442` n `419`
- 24h: commodity avg `-0.3326` n `12`; crypto_alt avg `0.9872` n `228`; crypto_major avg `1.3217` n `8`; equity avg `0.7659` n `69`; fx avg `0.1117` n `6`; index avg `0.0312` n `23`; metal avg `-0.1091` n `18`; unknown avg `1.4312` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
