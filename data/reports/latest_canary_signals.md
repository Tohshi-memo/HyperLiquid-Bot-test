# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T03:52:39.759052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.1645` n `230`; crypto_major avg `0.2143` n `8`; equity avg `-0.0771` n `121`; fx avg `-0.0126` n `6`; index avg `-0.0375` n `25`; metal avg `-0.0045` n `20`; unknown avg `0.0483` n `793`
- 1h: commodity avg `-0.0417` n `12`; crypto_alt avg `0.2625` n `230`; crypto_major avg `0.0053` n `8`; equity avg `-0.278` n `121`; fx avg `0.0137` n `6`; index avg `-0.0453` n `25`; metal avg `-0.1059` n `20`; unknown avg `0.8998` n `793`
- 4h: commodity avg `0.0396` n `12`; crypto_alt avg `1.0207` n `230`; crypto_major avg `1.3113` n `8`; equity avg `0.7916` n `121`; fx avg `-0.0805` n `6`; index avg `0.1521` n `25`; metal avg `0.1542` n `20`; unknown avg `-0.0456` n `793`
- 24h: commodity avg `0.3227` n `12`; crypto_alt avg `5.8628` n `230`; crypto_major avg `7.2281` n `8`; equity avg `-0.5891` n `121`; fx avg `-0.0026` n `6`; index avg `-0.119` n `25`; metal avg `0.4381` n `20`; unknown avg `2.6247` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1808`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
