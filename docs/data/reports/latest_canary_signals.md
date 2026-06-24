# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T12:52:32.799454+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.2757` n `228`; crypto_major avg `-0.3054` n `8`; equity avg `-0.1305` n `86`; fx avg `-0.0118` n `6`; index avg `-0.0278` n `23`; metal avg `-0.0484` n `20`; unknown avg `-0.0598` n `764`
- 1h: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.4065` n `228`; crypto_major avg `-0.5896` n `8`; equity avg `-0.3828` n `86`; fx avg `-0.0236` n `6`; index avg `-0.0497` n `23`; metal avg `-0.5426` n `20`; unknown avg `-0.0588` n `764`
- 4h: commodity avg `-0.1583` n `12`; crypto_alt avg `-0.2831` n `228`; crypto_major avg `-0.3923` n `8`; equity avg `-0.3197` n `86`; fx avg `-0.0649` n `6`; index avg `-0.0124` n `23`; metal avg `-1.0023` n `20`; unknown avg `-0.1192` n `764`
- 24h: commodity avg `-0.5908` n `12`; crypto_alt avg `0.0199` n `228`; crypto_major avg `-0.0017` n `8`; equity avg `4.5459` n `86`; fx avg `-0.036` n `6`; index avg `0.1683` n `23`; metal avg `-1.3929` n `20`; unknown avg `-0.1423` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
