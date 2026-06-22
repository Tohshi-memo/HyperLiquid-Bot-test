# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T11:37:32.166037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0621` n `12`; crypto_alt avg `0.3662` n `228`; crypto_major avg `0.4276` n `8`; equity avg `0.0832` n `79`; fx avg `0.0058` n `6`; index avg `0.0264` n `23`; metal avg `-0.0408` n `20`; unknown avg `0.1505` n `722`
- 1h: commodity avg `-0.1373` n `12`; crypto_alt avg `0.8034` n `228`; crypto_major avg `0.7235` n `8`; equity avg `0.2134` n `79`; fx avg `-0.0096` n `6`; index avg `0.0626` n `23`; metal avg `-0.0569` n `20`; unknown avg `0.7152` n `722`
- 4h: commodity avg `-0.1523` n `12`; crypto_alt avg `0.7306` n `228`; crypto_major avg `0.5595` n `8`; equity avg `0.2782` n `79`; fx avg `0.0105` n `6`; index avg `0.1131` n `23`; metal avg `0.0316` n `18`; unknown avg `0.5377` n `693`
- 24h: commodity avg `-0.259` n `12`; crypto_alt avg `0.8179` n `228`; crypto_major avg `0.9519` n `8`; equity avg `0.115` n `79`; fx avg `0.036` n `6`; index avg `0.1287` n `23`; metal avg `0.488` n `18`; unknown avg `0.9195` n `637`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
