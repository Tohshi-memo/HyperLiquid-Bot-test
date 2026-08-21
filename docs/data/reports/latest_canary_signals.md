# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T13:06:59.280051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.038` n `12`; crypto_alt avg `0.0093` n `230`; crypto_major avg `0.2272` n `8`; equity avg `-0.0686` n `121`; fx avg `0.0007` n `6`; index avg `-0.0068` n `25`; metal avg `0.0122` n `20`; unknown avg `0.0039` n `793`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `0.8333` n `230`; crypto_major avg `0.801` n `8`; equity avg `0.0636` n `121`; fx avg `-0.017` n `6`; index avg `0.0107` n `25`; metal avg `-0.0496` n `20`; unknown avg `0.0474` n `793`
- 4h: commodity avg `0.1545` n `12`; crypto_alt avg `2.6553` n `230`; crypto_major avg `0.9209` n `8`; equity avg `0.2509` n `121`; fx avg `0.0219` n `6`; index avg `0.0418` n `25`; metal avg `-0.0823` n `20`; unknown avg `0.2534` n `793`
- 24h: commodity avg `0.1424` n `12`; crypto_alt avg `8.0495` n `230`; crypto_major avg `6.3228` n `8`; equity avg `1.4761` n `121`; fx avg `-0.0888` n `6`; index avg `0.1922` n `25`; metal avg `0.8807` n `20`; unknown avg `2.2985` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2358`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1913`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
