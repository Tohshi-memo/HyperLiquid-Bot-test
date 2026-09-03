# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T06:27:53.544445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `12`; crypto_alt avg `0.1498` n `232`; crypto_major avg `0.1456` n `8`; equity avg `-0.1017` n `133`; fx avg `0.0096` n `6`; index avg `-0.0342` n `26`; metal avg `-0.0653` n `20`; unknown avg `-0.0369` n `792`
- 1h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.5768` n `232`; crypto_major avg `0.666` n `8`; equity avg `0.3939` n `133`; fx avg `-0.0575` n `6`; index avg `0.1032` n `26`; metal avg `0.0535` n `20`; unknown avg `14.94` n `756`
- 4h: commodity avg `-0.2254` n `12`; crypto_alt avg `0.6945` n `232`; crypto_major avg `0.3944` n `8`; equity avg `-0.2155` n `133`; fx avg `-0.0632` n `6`; index avg `-0.0641` n `26`; metal avg `0.0406` n `20`; unknown avg `0.16` n `756`
- 24h: commodity avg `-0.005` n `12`; crypto_alt avg `0.7334` n `232`; crypto_major avg `0.529` n `8`; equity avg `1.1777` n `133`; fx avg `-0.3494` n `6`; index avg `0.1367` n `26`; metal avg `0.7037` n `20`; unknown avg `-0.4566` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0398`, n `668`, weak_sample_signal
