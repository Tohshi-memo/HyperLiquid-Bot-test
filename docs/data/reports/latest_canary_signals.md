# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T15:52:40.620728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3011` n `12`; crypto_alt avg `0.0139` n `228`; crypto_major avg `-0.114` n `8`; equity avg `-0.1814` n `77`; fx avg `0.0136` n `6`; index avg `-0.2284` n `23`; metal avg `-0.0215` n `18`; unknown avg `0.0241` n `687`
- 1h: commodity avg `-0.2988` n `12`; crypto_alt avg `0.3117` n `228`; crypto_major avg `0.2411` n `8`; equity avg `-0.3248` n `77`; fx avg `0.0358` n `6`; index avg `-0.3491` n `23`; metal avg `0.0448` n `18`; unknown avg `0.68` n `687`
- 4h: commodity avg `-0.4901` n `12`; crypto_alt avg `-1.1858` n `228`; crypto_major avg `-1.0474` n `8`; equity avg `-1.4677` n `77`; fx avg `0.04` n `6`; index avg `-0.8873` n `23`; metal avg `-0.2807` n `18`; unknown avg `0.7717` n `687`
- 24h: commodity avg `-0.733` n `12`; crypto_alt avg `-2.5061` n `228`; crypto_major avg `-1.3464` n `8`; equity avg `2.0775` n `77`; fx avg `-0.0158` n `6`; index avg `-0.8317` n `23`; metal avg `-0.3313` n `18`; unknown avg `0.4803` n `623`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.062`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0464`, n `668`, weak_sample_signal
