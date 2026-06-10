# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T09:52:36.086008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2037` n `12`; crypto_alt avg `0.0181` n `228`; crypto_major avg `-0.0333` n `8`; equity avg `0.003` n `74`; fx avg `0.0079` n `6`; index avg `-0.0488` n `23`; metal avg `-0.1665` n `18`; unknown avg `0.2052` n `547`
- 1h: commodity avg `0.3656` n `12`; crypto_alt avg `-0.1777` n `228`; crypto_major avg `-0.0046` n `8`; equity avg `-0.0699` n `74`; fx avg `0.039` n `6`; index avg `0.0411` n `23`; metal avg `-0.0996` n `18`; unknown avg `0.094` n `547`
- 4h: commodity avg `0.5966` n `12`; crypto_alt avg `0.0933` n `228`; crypto_major avg `-0.1363` n `8`; equity avg `-0.3304` n `74`; fx avg `0.0112` n `6`; index avg `-0.1855` n `23`; metal avg `-0.3561` n `18`; unknown avg `-0.1288` n `537`
- 24h: commodity avg `-0.1029` n `12`; crypto_alt avg `-1.3564` n `228`; crypto_major avg `-3.6057` n `8`; equity avg `-4.3503` n `74`; fx avg `0.0509` n `6`; index avg `-2.354` n `23`; metal avg `-3.4919` n `18`; unknown avg `0.3791` n `535`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
