# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T13:07:30.708995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1286` n `12`; crypto_alt avg `-0.0958` n `234`; crypto_major avg `-0.1776` n `8`; equity avg `-0.0484` n `140`; fx avg `-0.0118` n `6`; index avg `-0.0052` n `26`; metal avg `0.0026` n `20`; unknown avg `0.1326` n `926`
- 1h: commodity avg `0.1682` n `12`; crypto_alt avg `0.242` n `234`; crypto_major avg `0.0798` n `8`; equity avg `-0.0884` n `140`; fx avg `-0.0116` n `6`; index avg `-0.0246` n `26`; metal avg `-0.0763` n `20`; unknown avg `0.2249` n `920`
- 4h: commodity avg `0.3592` n `12`; crypto_alt avg `-0.0322` n `234`; crypto_major avg `-0.1594` n `8`; equity avg `-0.6332` n `140`; fx avg `-0.035` n `6`; index avg `-0.1098` n `26`; metal avg `-0.2063` n `20`; unknown avg `1.0347` n `917`
- 24h: commodity avg `0.3098` n `12`; crypto_alt avg `5.2387` n `234`; crypto_major avg `3.6341` n `8`; equity avg `0.5486` n `140`; fx avg `0.225` n `6`; index avg `-0.0471` n `26`; metal avg `0.2275` n `20`; unknown avg `1.1211` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1371`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1317`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
