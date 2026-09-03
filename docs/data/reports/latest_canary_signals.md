# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T07:37:26.627194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `-0.0011` n `232`; crypto_major avg `-0.0997` n `8`; equity avg `0.0017` n `133`; fx avg `0.0563` n `6`; index avg `0.0063` n `26`; metal avg `0.0196` n `20`; unknown avg `19.7728` n `792`
- 1h: commodity avg `0.0198` n `12`; crypto_alt avg `0.2203` n `232`; crypto_major avg `0.1263` n `8`; equity avg `0.0973` n `133`; fx avg `-0.017` n `6`; index avg `-0.0055` n `26`; metal avg `0.0457` n `20`; unknown avg `0.0185` n `790`
- 4h: commodity avg `-0.1508` n `12`; crypto_alt avg `0.7118` n `232`; crypto_major avg `0.3599` n `8`; equity avg `-0.2917` n `133`; fx avg `-0.0797` n `6`; index avg `-0.1198` n `26`; metal avg `-0.0003` n `20`; unknown avg `15.08` n `754`
- 24h: commodity avg `0.1514` n `12`; crypto_alt avg `0.7259` n `232`; crypto_major avg `0.5657` n `8`; equity avg `1.1346` n `133`; fx avg `-0.3546` n `6`; index avg `0.0716` n `26`; metal avg `0.6995` n `20`; unknown avg `-0.2636` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0529`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0386`, n `668`, weak_sample_signal
