# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T16:22:33.804878+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0281` n `12`; crypto_alt avg `-0.1026` n `228`; crypto_major avg `-0.1079` n `8`; equity avg `-0.0554` n `86`; fx avg `0.0122` n `6`; index avg `0.0073` n `23`; metal avg `0.0193` n `20`; unknown avg `0.1303` n `764`
- 1h: commodity avg `-0.0617` n `12`; crypto_alt avg `0.2361` n `228`; crypto_major avg `0.4803` n `8`; equity avg `0.4384` n `86`; fx avg `-0.0113` n `6`; index avg `0.0363` n `23`; metal avg `0.1522` n `20`; unknown avg `0.1965` n `764`
- 4h: commodity avg `-0.1613` n `12`; crypto_alt avg `0.0609` n `228`; crypto_major avg `-0.0346` n `8`; equity avg `0.9482` n `86`; fx avg `-0.0571` n `6`; index avg `0.0674` n `23`; metal avg `0.2801` n `20`; unknown avg `-0.1899` n `764`
- 24h: commodity avg `-0.4174` n `12`; crypto_alt avg `-3.7145` n `228`; crypto_major avg `-3.8892` n `8`; equity avg `-2.724` n `86`; fx avg `-0.182` n `6`; index avg `-0.8689` n `23`; metal avg `-0.8257` n `20`; unknown avg `-0.1307` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
