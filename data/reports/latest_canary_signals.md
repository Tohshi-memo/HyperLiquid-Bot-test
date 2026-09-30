# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T23:22:29.711313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `12`; crypto_alt avg `0.0512` n `234`; crypto_major avg `0.0291` n `8`; equity avg `0.0212` n `142`; fx avg `0.0127` n `6`; index avg `0.0094` n `26`; metal avg `0.004` n `20`; unknown avg `3.6271` n `975`
- 1h: commodity avg `-0.0314` n `12`; crypto_alt avg `0.4655` n `234`; crypto_major avg `0.1072` n `8`; equity avg `0.0925` n `142`; fx avg `0.0148` n `6`; index avg `0.0344` n `26`; metal avg `-0.0232` n `20`; unknown avg `0.0456` n `973`
- 4h: commodity avg `-0.094` n `12`; crypto_alt avg `0.6495` n `234`; crypto_major avg `0.4806` n `8`; equity avg `-0.0194` n `142`; fx avg `0.0358` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0216` n `20`; unknown avg `2.217` n `887`
- 24h: commodity avg `0.1596` n `12`; crypto_alt avg `0.5933` n `234`; crypto_major avg `0.8222` n `8`; equity avg `-0.3363` n `142`; fx avg `0.0935` n `6`; index avg `-0.0118` n `26`; metal avg `-0.2722` n `20`; unknown avg `764.5688` n `813`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
