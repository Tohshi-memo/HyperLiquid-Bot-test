# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T23:52:17.960500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `0.3614` n `228`; crypto_major avg `0.3081` n `8`; equity avg `0.0569` n `69`; fx avg `-0.0086` n `6`; index avg `0.0569` n `23`; metal avg `0.0633` n `18`; unknown avg `0.1123` n `421`
- 1h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.2238` n `228`; crypto_major avg `-0.3747` n `8`; equity avg `-0.006` n `69`; fx avg `-0.0058` n `6`; index avg `-0.129` n `23`; metal avg `0.3101` n `18`; unknown avg `-0.2324` n `421`
- 4h: commodity avg `0.1925` n `12`; crypto_alt avg `1.508` n `228`; crypto_major avg `0.9424` n `8`; equity avg `0.0148` n `69`; fx avg `-0.0208` n `6`; index avg `-0.0823` n `23`; metal avg `0.391` n `18`; unknown avg `1.5118` n `421`
- 24h: commodity avg `0.8883` n `12`; crypto_alt avg `0.9842` n `228`; crypto_major avg `0.3476` n `8`; equity avg `0.6691` n `69`; fx avg `-0.0122` n `6`; index avg `0.1181` n `23`; metal avg `0.2743` n `18`; unknown avg `2.0627` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.323`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2558`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
