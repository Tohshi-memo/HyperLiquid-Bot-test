# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T22:07:35.615662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0227` n `12`; crypto_alt avg `0.1301` n `229`; crypto_major avg `0.0792` n `8`; equity avg `0.0125` n `92`; fx avg `-0.0035` n `6`; index avg `-0.0001` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.1351` n `765`
- 1h: commodity avg `-0.046` n `12`; crypto_alt avg `0.4092` n `229`; crypto_major avg `0.1632` n `8`; equity avg `0.0209` n `92`; fx avg `-0.0026` n `6`; index avg `-0.0038` n `25`; metal avg `-0.0321` n `20`; unknown avg `-0.0485` n `765`
- 4h: commodity avg `0.1058` n `12`; crypto_alt avg `0.419` n `229`; crypto_major avg `0.1373` n `8`; equity avg `-0.1752` n `92`; fx avg `-0.0146` n `6`; index avg `-0.0045` n `25`; metal avg `0.1021` n `20`; unknown avg `-0.3977` n `765`
- 24h: commodity avg `-0.2567` n `12`; crypto_alt avg `1.1773` n `229`; crypto_major avg `0.9539` n `8`; equity avg `-0.6558` n `92`; fx avg `-0.1744` n `6`; index avg `0.0346` n `25`; metal avg `0.1444` n `20`; unknown avg `-0.1831` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
