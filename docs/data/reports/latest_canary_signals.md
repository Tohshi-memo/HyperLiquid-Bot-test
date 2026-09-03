# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T12:52:27.741830+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1309` n `12`; crypto_alt avg `0.0389` n `232`; crypto_major avg `0.0833` n `8`; equity avg `0.1568` n `133`; fx avg `-0.004` n `6`; index avg `0.036` n `26`; metal avg `0.115` n `20`; unknown avg `0.2247` n `792`
- 1h: commodity avg `-0.2228` n `12`; crypto_alt avg `0.2513` n `232`; crypto_major avg `0.4432` n `8`; equity avg `0.5256` n `133`; fx avg `-0.046` n `6`; index avg `0.1252` n `26`; metal avg `0.3254` n `20`; unknown avg `1.1641` n `790`
- 4h: commodity avg `0.0939` n `12`; crypto_alt avg `0.4901` n `232`; crypto_major avg `0.7963` n `8`; equity avg `0.2233` n `133`; fx avg `-0.0929` n `6`; index avg `0.0531` n `26`; metal avg `0.2815` n `20`; unknown avg `2.3722` n `790`
- 24h: commodity avg `0.4728` n `12`; crypto_alt avg `2.6378` n `232`; crypto_major avg `2.7108` n `8`; equity avg `1.6071` n `133`; fx avg `-0.4287` n `6`; index avg `0.1709` n `26`; metal avg `0.9382` n `20`; unknown avg `-0.0012` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0408`, n `668`, weak_sample_signal
