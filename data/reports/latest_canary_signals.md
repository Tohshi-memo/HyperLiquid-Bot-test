# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T23:07:29.546236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0222` n `12`; crypto_alt avg `-0.0357` n `234`; crypto_major avg `-0.125` n `8`; equity avg `0.0051` n `141`; fx avg `-0.001` n `6`; index avg `0.0041` n `26`; metal avg `-0.0116` n `20`; unknown avg `-0.1086` n `958`
- 1h: commodity avg `0.0059` n `12`; crypto_alt avg `0.9153` n `234`; crypto_major avg `0.5244` n `8`; equity avg `0.0244` n `141`; fx avg `0.0134` n `6`; index avg `0.002` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.5343` n `942`
- 4h: commodity avg `0.1018` n `12`; crypto_alt avg `0.6672` n `234`; crypto_major avg `0.3462` n `8`; equity avg `-0.0731` n `141`; fx avg `0.0001` n `6`; index avg `0.0201` n `26`; metal avg `-0.0427` n `20`; unknown avg `0.0598` n `852`
- 24h: commodity avg `-0.4148` n `12`; crypto_alt avg `2.8414` n `234`; crypto_major avg `1.2649` n `8`; equity avg `0.1267` n `141`; fx avg `-0.2522` n `6`; index avg `0.2677` n `26`; metal avg `0.1438` n `20`; unknown avg `1124.7636` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
