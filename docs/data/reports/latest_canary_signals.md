# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T16:52:30.307511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0137` n `12`; crypto_alt avg `0.127` n `230`; crypto_major avg `0.1754` n `8`; equity avg `-0.0207` n `121`; fx avg `-0.0034` n `6`; index avg `-0.0075` n `25`; metal avg `0.0425` n `20`; unknown avg `0.2758` n `793`
- 1h: commodity avg `0.002` n `12`; crypto_alt avg `0.2543` n `230`; crypto_major avg `0.1366` n `8`; equity avg `-0.2919` n `121`; fx avg `0.007` n `6`; index avg `-0.0695` n `25`; metal avg `0.0887` n `20`; unknown avg `1.5714` n `793`
- 4h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.7643` n `230`; crypto_major avg `0.8665` n `8`; equity avg `-0.5858` n `121`; fx avg `0.0021` n `6`; index avg `-0.0788` n `25`; metal avg `0.0869` n `20`; unknown avg `1.4477` n `793`
- 24h: commodity avg `0.3249` n `12`; crypto_alt avg `7.1378` n `230`; crypto_major avg `4.1035` n `8`; equity avg `1.1521` n `121`; fx avg `-0.0971` n `6`; index avg `0.06` n `25`; metal avg `0.6625` n `20`; unknown avg `2.9124` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2379`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
