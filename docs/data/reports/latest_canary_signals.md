# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T09:52:29.157407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0388` n `12`; crypto_alt avg `-0.1142` n `232`; crypto_major avg `-0.3439` n `8`; equity avg `0.0797` n `133`; fx avg `-0.0047` n `6`; index avg `0.0153` n `26`; metal avg `0.005` n `20`; unknown avg `-0.1337` n `793`
- 1h: commodity avg `0.0416` n `12`; crypto_alt avg `0.3833` n `232`; crypto_major avg `0.0046` n `8`; equity avg `0.0709` n `133`; fx avg `-0.0052` n `6`; index avg `0.0046` n `26`; metal avg `-0.1133` n `20`; unknown avg `-0.0549` n `791`
- 4h: commodity avg `-0.0758` n `12`; crypto_alt avg `1.2759` n `232`; crypto_major avg `0.4202` n `8`; equity avg `0.264` n `133`; fx avg `-0.0149` n `6`; index avg `0.0058` n `26`; metal avg `0.0229` n `20`; unknown avg `-0.2028` n `749`
- 24h: commodity avg `-0.3327` n `12`; crypto_alt avg `2.8435` n `232`; crypto_major avg `4.2295` n `8`; equity avg `2.2361` n `133`; fx avg `0.006` n `6`; index avg `0.398` n `26`; metal avg `0.4476` n `20`; unknown avg `1.6422` n `730`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
