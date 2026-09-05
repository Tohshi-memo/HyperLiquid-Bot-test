# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T18:52:23.595687+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0096` n `12`; crypto_alt avg `-0.0975` n `232`; crypto_major avg `-0.1233` n `8`; equity avg `-0.0045` n `134`; fx avg `0.0032` n `6`; index avg `0.0155` n `26`; metal avg `0.0005` n `20`; unknown avg `18.8408` n `794`
- 1h: commodity avg `0.0201` n `12`; crypto_alt avg `0.0166` n `232`; crypto_major avg `0.251` n `8`; equity avg `-0.0062` n `134`; fx avg `-0.0026` n `6`; index avg `0.0076` n `26`; metal avg `-0.003` n `20`; unknown avg `18.8116` n `792`
- 4h: commodity avg `0.0244` n `12`; crypto_alt avg `0.4357` n `232`; crypto_major avg `1.0831` n `8`; equity avg `0.1186` n `134`; fx avg `-0.0248` n `6`; index avg `0.0334` n `26`; metal avg `0.0399` n `20`; unknown avg `-0.4903` n `786`
- 24h: commodity avg `-0.0722` n `12`; crypto_alt avg `2.7184` n `232`; crypto_major avg `2.8321` n `8`; equity avg `0.4476` n `134`; fx avg `-0.0326` n `6`; index avg `0.0464` n `26`; metal avg `0.1314` n `20`; unknown avg `0.2055` n `658`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
