# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T18:07:28.729488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `12`; crypto_alt avg `0.2871` n `230`; crypto_major avg `0.1205` n `8`; equity avg `-0.074` n `121`; fx avg `0.0111` n `6`; index avg `-0.0055` n `25`; metal avg `0.038` n `20`; unknown avg `-0.0239` n `793`
- 1h: commodity avg `0.0413` n `12`; crypto_alt avg `-0.07` n `230`; crypto_major avg `-0.3721` n `8`; equity avg `-0.1066` n `121`; fx avg `0.0154` n `6`; index avg `-0.0407` n `25`; metal avg `-0.0588` n `20`; unknown avg `-0.0959` n `793`
- 4h: commodity avg `0.1369` n `12`; crypto_alt avg `0.6994` n `230`; crypto_major avg `0.4147` n `8`; equity avg `-0.226` n `121`; fx avg `0.0256` n `6`; index avg `0.0156` n `25`; metal avg `0.0568` n `20`; unknown avg `0.0458` n `793`
- 24h: commodity avg `0.3577` n `12`; crypto_alt avg `7.6435` n `230`; crypto_major avg `4.4617` n `8`; equity avg `1.4173` n `121`; fx avg `-0.0813` n `6`; index avg `0.1394` n `25`; metal avg `0.6404` n `20`; unknown avg `1.1929` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2326`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.2009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
