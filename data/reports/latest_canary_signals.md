# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T00:52:30.185946+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `13`; crypto_alt avg `-0.1623` n `238`; crypto_major avg `-0.1081` n `8`; equity avg `0.0475` n `155`; fx avg `0.0008` n `6`; index avg `0.0123` n `27`; metal avg `-0.0192` n `20`; unknown avg `0.0338` n `1238`
- 1h: commodity avg `0.0218` n `13`; crypto_alt avg `-0.1539` n `238`; crypto_major avg `-0.1937` n `8`; equity avg `0.482` n `155`; fx avg `-0.0827` n `6`; index avg `0.1004` n `27`; metal avg `-0.1145` n `20`; unknown avg `0.6276` n `1222`
- 4h: commodity avg `-0.0358` n `13`; crypto_alt avg `-0.3575` n `238`; crypto_major avg `-0.2021` n `8`; equity avg `0.3798` n `155`; fx avg `-0.1113` n `6`; index avg `0.0586` n `27`; metal avg `-0.1381` n `20`; unknown avg `9.2485` n `1144`
- 24h: commodity avg `0.0744` n `13`; crypto_alt avg `0.1442` n `238`; crypto_major avg `0.2277` n `8`; equity avg `0.6038` n `154`; fx avg `0.0936` n `6`; index avg `0.1192` n `27`; metal avg `-0.26` n `20`; unknown avg `24.7509` n `996`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
