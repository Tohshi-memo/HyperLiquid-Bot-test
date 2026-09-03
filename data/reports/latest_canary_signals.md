# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T06:52:25.973600+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.0231` n `232`; crypto_major avg `0.0086` n `8`; equity avg `-0.0267` n `133`; fx avg `-0.0421` n `6`; index avg `-0.0012` n `26`; metal avg `0.0021` n `20`; unknown avg `-0.0199` n `792`
- 1h: commodity avg `0.0139` n `12`; crypto_alt avg `0.1518` n `232`; crypto_major avg `0.1598` n `8`; equity avg `-0.0149` n `133`; fx avg `-0.085` n `6`; index avg `-0.0229` n `26`; metal avg `-0.0419` n `20`; unknown avg `-0.0999` n `754`
- 4h: commodity avg `-0.183` n `12`; crypto_alt avg `0.173` n `232`; crypto_major avg `-0.0782` n `8`; equity avg `-0.2237` n `133`; fx avg `-0.1019` n `6`; index avg `-0.0784` n `26`; metal avg `0.0456` n `20`; unknown avg `-0.0776` n `754`
- 24h: commodity avg `-0.0289` n `12`; crypto_alt avg `0.5389` n `232`; crypto_major avg `0.4981` n `8`; equity avg `1.1617` n `133`; fx avg `-0.3608` n `6`; index avg `0.105` n `26`; metal avg `0.725` n `20`; unknown avg `-0.3351` n `735`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0388`, n `668`, weak_sample_signal
