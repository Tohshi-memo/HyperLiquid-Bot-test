# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T13:22:29.322149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0151` n `13`; crypto_alt avg `-0.0647` n `238`; crypto_major avg `-0.0354` n `8`; equity avg `-0.1916` n `154`; fx avg `-0.0041` n `6`; index avg `-0.0143` n `27`; metal avg `-0.0453` n `20`; unknown avg `0.3709` n `1237`
- 1h: commodity avg `0.0623` n `13`; crypto_alt avg `-0.2124` n `238`; crypto_major avg `-0.3257` n `8`; equity avg `-0.2927` n `154`; fx avg `-0.0284` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0118` n `20`; unknown avg `1.6464` n `1233`
- 4h: commodity avg `0.1779` n `13`; crypto_alt avg `-0.9395` n `238`; crypto_major avg `-0.9483` n `8`; equity avg `-0.3831` n `154`; fx avg `0.0427` n `6`; index avg `0.0329` n `27`; metal avg `-0.0011` n `20`; unknown avg `1.2794` n `1210`
- 24h: commodity avg `0.2419` n `13`; crypto_alt avg `0.9074` n `238`; crypto_major avg `0.8827` n `8`; equity avg `2.4277` n `154`; fx avg `0.105` n `6`; index avg `0.4085` n `27`; metal avg `0.2474` n `20`; unknown avg `6.6416` n `1066`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
