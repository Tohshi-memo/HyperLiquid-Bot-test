# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T15:55:59.279708+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0823` n `12`; crypto_alt avg `-0.068` n `230`; crypto_major avg `-0.0445` n `8`; equity avg `-0.0327` n `98`; fx avg `-0.0016` n `6`; index avg `0.0201` n `25`; metal avg `0.0342` n `20`; unknown avg `-0.0221` n `773`
- 1h: commodity avg `-0.1136` n `12`; crypto_alt avg `0.2634` n `230`; crypto_major avg `0.363` n `8`; equity avg `0.403` n `98`; fx avg `0.0016` n `6`; index avg `0.105` n `25`; metal avg `0.0939` n `20`; unknown avg `-0.1252` n `773`
- 4h: commodity avg `-0.1727` n `12`; crypto_alt avg `0.3252` n `230`; crypto_major avg `0.3814` n `8`; equity avg `1.2869` n `98`; fx avg `-0.0172` n `6`; index avg `0.25` n `25`; metal avg `0.1955` n `20`; unknown avg `9.4593` n `773`
- 24h: commodity avg `0.3338` n `12`; crypto_alt avg `-0.242` n `230`; crypto_major avg `-0.9249` n `8`; equity avg `0.3123` n `98`; fx avg `-0.0263` n `6`; index avg `-0.0092` n `25`; metal avg `0.4881` n `20`; unknown avg `1.0766` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.105`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0911`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0706`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0706`, n `666`, weak_sample_signal
