# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T20:52:29.938452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.2964` n `234`; crypto_major avg `-0.1907` n `8`; equity avg `0.01` n `141`; fx avg `-0.0041` n `6`; index avg `-0.0005` n `26`; metal avg `0.0197` n `20`; unknown avg `1.4776` n `960`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `0.2536` n `234`; crypto_major avg `-0.0546` n `8`; equity avg `-0.0313` n `141`; fx avg `-0.0086` n `6`; index avg `-0.0159` n `26`; metal avg `-0.0028` n `20`; unknown avg `1.2777` n `878`
- 4h: commodity avg `0.1194` n `12`; crypto_alt avg `0.7432` n `234`; crypto_major avg `0.1278` n `8`; equity avg `-0.1671` n `141`; fx avg `-0.0084` n `6`; index avg `0.0269` n `26`; metal avg `0.0313` n `20`; unknown avg `0.2241` n `878`
- 24h: commodity avg `-0.6516` n `12`; crypto_alt avg `2.4012` n `234`; crypto_major avg `0.6825` n `8`; equity avg `0.1368` n `141`; fx avg `-0.2452` n `6`; index avg `0.2428` n `26`; metal avg `0.1769` n `20`; unknown avg `1148.0404` n `794`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1735`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
