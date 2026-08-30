# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T08:22:23.908488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0037` n `12`; crypto_alt avg `0.0145` n `231`; crypto_major avg `0.0338` n `8`; equity avg `0.0084` n `128`; fx avg `0.0` n `6`; index avg `-0.0015` n `26`; metal avg `0.0011` n `20`; unknown avg `-0.0174` n `793`
- 1h: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.058` n `231`; crypto_major avg `-0.0949` n `8`; equity avg `-0.0161` n `128`; fx avg `-0.0017` n `6`; index avg `-0.0157` n `26`; metal avg `0.0051` n `20`; unknown avg `-0.0901` n `793`
- 4h: commodity avg `-0.0018` n `12`; crypto_alt avg `0.1761` n `231`; crypto_major avg `0.0315` n `8`; equity avg `-0.0025` n `128`; fx avg `0.0044` n `6`; index avg `-0.0002` n `26`; metal avg `0.0181` n `20`; unknown avg `-0.0764` n `759`
- 24h: commodity avg `-0.011` n `12`; crypto_alt avg `0.954` n `231`; crypto_major avg `0.9943` n `8`; equity avg `0.2663` n `128`; fx avg `-0.0095` n `6`; index avg `0.0517` n `26`; metal avg `0.1022` n `20`; unknown avg `0.713` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1625`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
