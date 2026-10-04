# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T14:07:27.549798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1683` n `13`; crypto_alt avg `-0.0804` n `235`; crypto_major avg `-0.121` n `8`; equity avg `0.0035` n `144`; fx avg `-0.0022` n `6`; index avg `0.0002` n `26`; metal avg `0.0024` n `20`; unknown avg `0.0511` n `1076`
- 1h: commodity avg `-0.1574` n `13`; crypto_alt avg `-0.0884` n `235`; crypto_major avg `-0.0075` n `8`; equity avg `0.027` n `144`; fx avg `0.0022` n `6`; index avg `0.0033` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.287` n `1076`
- 4h: commodity avg `-0.1134` n `13`; crypto_alt avg `-0.268` n `235`; crypto_major avg `-0.1846` n `8`; equity avg `0.0443` n `144`; fx avg `0.0234` n `6`; index avg `-0.0022` n `26`; metal avg `-0.0064` n `20`; unknown avg `0.0972` n `1070`
- 24h: commodity avg `-0.0593` n `13`; crypto_alt avg `1.3993` n `235`; crypto_major avg `1.0999` n `8`; equity avg `0.2969` n `144`; fx avg `0.0079` n `6`; index avg `0.0264` n `26`; metal avg `0.0012` n `20`; unknown avg `0.0212` n `915`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.206`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
