# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T03:52:29.042171+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.1062` n `228`; crypto_major avg `0.0708` n `8`; equity avg `0.0458` n `86`; fx avg `0.0206` n `6`; index avg `-0.0035` n `23`; metal avg `0.2646` n `20`; unknown avg `1.3646` n `765`
- 1h: commodity avg `-0.0588` n `12`; crypto_alt avg `-0.0167` n `228`; crypto_major avg `-0.0352` n `8`; equity avg `0.1146` n `86`; fx avg `0.006` n `6`; index avg `0.0105` n `23`; metal avg `0.2412` n `20`; unknown avg `-0.5875` n `764`
- 4h: commodity avg `-0.1218` n `12`; crypto_alt avg `-0.1998` n `228`; crypto_major avg `-0.3471` n `8`; equity avg `-0.7679` n `86`; fx avg `0.0626` n `6`; index avg `-0.0389` n `23`; metal avg `-0.1385` n `20`; unknown avg `0.2936` n `748`
- 24h: commodity avg `-0.4683` n `12`; crypto_alt avg `-1.9738` n `228`; crypto_major avg `-1.9171` n `8`; equity avg `0.1269` n `86`; fx avg `0.0789` n `6`; index avg `0.6396` n `23`; metal avg `-1.4277` n `20`; unknown avg `-0.5716` n `700`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0624`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
