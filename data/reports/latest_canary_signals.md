# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T07:52:30.168207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.192` n `12`; crypto_alt avg `0.0259` n `228`; crypto_major avg `-0.0127` n `8`; equity avg `0.0368` n `74`; fx avg `-0.0094` n `6`; index avg `0.0153` n `23`; metal avg `0.0021` n `18`; unknown avg `0.0612` n `645`
- 1h: commodity avg `-0.2644` n `12`; crypto_alt avg `-0.0014` n `228`; crypto_major avg `0.014` n `8`; equity avg `0.0886` n `74`; fx avg `-0.0007` n `6`; index avg `0.0063` n `23`; metal avg `-0.0101` n `18`; unknown avg `0.051` n `645`
- 4h: commodity avg `-0.3535` n `12`; crypto_alt avg `-0.509` n `228`; crypto_major avg `-0.4637` n `8`; equity avg `0.0826` n `74`; fx avg `-0.0146` n `6`; index avg `-0.0002` n `23`; metal avg `0.0169` n `18`; unknown avg `2.5595` n `625`
- 24h: commodity avg `-0.986` n `12`; crypto_alt avg `0.243` n `228`; crypto_major avg `0.7327` n `8`; equity avg `0.6435` n `74`; fx avg `-0.0179` n `6`; index avg `0.264` n `23`; metal avg `0.235` n `18`; unknown avg `-0.8235` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
