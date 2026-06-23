# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T20:22:46.796048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `0.0478` n `228`; crypto_major avg `-0.0224` n `8`; equity avg `0.1093` n `86`; fx avg `0.0027` n `6`; index avg `0.0106` n `23`; metal avg `-0.0356` n `20`; unknown avg `-0.0305` n `764`
- 1h: commodity avg `0.0341` n `12`; crypto_alt avg `0.5034` n `228`; crypto_major avg `0.427` n `8`; equity avg `0.2021` n `86`; fx avg `0.0019` n `6`; index avg `0.0172` n `23`; metal avg `-0.0441` n `20`; unknown avg `0.4042` n `764`
- 4h: commodity avg `0.0219` n `12`; crypto_alt avg `0.2169` n `228`; crypto_major avg `-0.0664` n `8`; equity avg `-0.697` n `86`; fx avg `-0.0008` n `6`; index avg `-0.1162` n `23`; metal avg `-0.3096` n `20`; unknown avg `-0.1495` n `756`
- 24h: commodity avg `-0.3635` n `12`; crypto_alt avg `-2.7649` n `228`; crypto_major avg `-3.6233` n `8`; equity avg `-3.3199` n `86`; fx avg `-0.191` n `6`; index avg `-0.9449` n `23`; metal avg `-1.2167` n `20`; unknown avg `0.2835` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
