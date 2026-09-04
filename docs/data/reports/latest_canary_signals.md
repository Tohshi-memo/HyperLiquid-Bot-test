# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T02:22:28.031742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.0629` n `232`; crypto_major avg `-0.0462` n `8`; equity avg `-0.0433` n `133`; fx avg `-0.0016` n `6`; index avg `0.0133` n `26`; metal avg `-0.0632` n `20`; unknown avg `-0.0903` n `793`
- 1h: commodity avg `-0.0474` n `12`; crypto_alt avg `-0.2172` n `232`; crypto_major avg `-0.1554` n `8`; equity avg `-0.0039` n `133`; fx avg `-0.006` n `6`; index avg `0.0096` n `26`; metal avg `-0.0436` n `20`; unknown avg `-0.1854` n `791`
- 4h: commodity avg `-0.0327` n `12`; crypto_alt avg `-0.7642` n `232`; crypto_major avg `-0.4559` n `8`; equity avg `0.3212` n `133`; fx avg `0.0355` n `6`; index avg `0.02` n `26`; metal avg `-0.0836` n `20`; unknown avg `2.1415` n `784`
- 24h: commodity avg `-0.2101` n `12`; crypto_alt avg `2.8698` n `232`; crypto_major avg `4.1796` n `8`; equity avg `1.4165` n `133`; fx avg `-0.1232` n `6`; index avg `0.2028` n `26`; metal avg `0.581` n `20`; unknown avg `1.1728` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
