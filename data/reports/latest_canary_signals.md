# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T20:52:30.719866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `13`; crypto_alt avg `0.196` n `235`; crypto_major avg `0.1117` n `8`; equity avg `0.0164` n `150`; fx avg `0.0005` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.517` n `1117`
- 1h: commodity avg `-0.0` n `13`; crypto_alt avg `0.3584` n `235`; crypto_major avg `0.0613` n `8`; equity avg `0.0091` n `150`; fx avg `0.0003` n `6`; index avg `0.0113` n `26`; metal avg `0.0029` n `20`; unknown avg `2.8039` n `1101`
- 4h: commodity avg `0.0204` n `13`; crypto_alt avg `0.4315` n `235`; crypto_major avg `0.1249` n `8`; equity avg `0.0471` n `150`; fx avg `-0.0035` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0015` n `20`; unknown avg `1.1457` n `999`
- 24h: commodity avg `-0.1943` n `13`; crypto_alt avg `3.1688` n `235`; crypto_major avg `1.2141` n `8`; equity avg `0.1742` n `150`; fx avg `-0.0091` n `6`; index avg `0.0129` n `26`; metal avg `-0.0293` n `20`; unknown avg `0.8162` n `964`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
