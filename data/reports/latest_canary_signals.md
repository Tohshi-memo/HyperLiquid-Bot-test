# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T09:52:28.011099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0038` n `12`; crypto_alt avg `0.0268` n `234`; crypto_major avg `0.1662` n `8`; equity avg `0.0182` n `141`; fx avg `0.0015` n `6`; index avg `-0.0002` n `26`; metal avg `0.0043` n `20`; unknown avg `0.152` n `961`
- 1h: commodity avg `0.0183` n `12`; crypto_alt avg `0.0149` n `234`; crypto_major avg `0.0551` n `8`; equity avg `0.0186` n `141`; fx avg `0.0035` n `6`; index avg `-0.0034` n `26`; metal avg `0.0098` n `20`; unknown avg `0.3821` n `959`
- 4h: commodity avg `-0.0153` n `12`; crypto_alt avg `0.8964` n `234`; crypto_major avg `0.9079` n `8`; equity avg `0.192` n `141`; fx avg `-0.0152` n `6`; index avg `0.0315` n `26`; metal avg `0.0136` n `20`; unknown avg `1.9029` n `923`
- 24h: commodity avg `0.0652` n `12`; crypto_alt avg `1.5091` n `234`; crypto_major avg `1.1946` n `8`; equity avg `0.4488` n `141`; fx avg `-0.003` n `6`; index avg `0.0376` n `26`; metal avg `0.0072` n `20`; unknown avg `5.4488` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
