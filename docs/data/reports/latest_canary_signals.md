# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T09:22:27.739363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0187` n `12`; crypto_alt avg `0.0228` n `232`; crypto_major avg `-0.0347` n `8`; equity avg `-0.0752` n `133`; fx avg `-0.0037` n `6`; index avg `-0.0183` n `26`; metal avg `-0.0909` n `20`; unknown avg `3.4795` n `793`
- 1h: commodity avg `0.0222` n `12`; crypto_alt avg `0.6323` n `232`; crypto_major avg `0.4723` n `8`; equity avg `-0.0242` n `133`; fx avg `-0.0114` n `6`; index avg `-0.0125` n `26`; metal avg `-0.1651` n `20`; unknown avg `3.4776` n `785`
- 4h: commodity avg `-0.0668` n `12`; crypto_alt avg `0.6811` n `232`; crypto_major avg `0.1735` n `8`; equity avg `-0.0826` n `133`; fx avg `0.0003` n `6`; index avg `-0.0433` n `26`; metal avg `-0.0337` n `20`; unknown avg `3.9023` n `749`
- 24h: commodity avg `-0.2874` n `12`; crypto_alt avg `2.665` n `232`; crypto_major avg `4.1777` n `8`; equity avg `2.0287` n `133`; fx avg `-0.026` n `6`; index avg `0.3376` n `26`; metal avg `0.3602` n `20`; unknown avg `4.4114` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
