# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T03:07:23.945376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.1634` n `230`; crypto_major avg `-0.7026` n `8`; equity avg `-0.2061` n `121`; fx avg `-0.0106` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0679` n `20`; unknown avg `0.4548` n `793`
- 1h: commodity avg `-0.0318` n `12`; crypto_alt avg `-0.1003` n `230`; crypto_major avg `-0.6872` n `8`; equity avg `-0.0011` n `121`; fx avg `0.0064` n `6`; index avg `0.0241` n `25`; metal avg `0.0858` n `20`; unknown avg `-0.016` n `793`
- 4h: commodity avg `0.0688` n `12`; crypto_alt avg `0.8338` n `230`; crypto_major avg `0.9672` n `8`; equity avg `0.7825` n `121`; fx avg `-0.127` n `6`; index avg `0.1209` n `25`; metal avg `0.2044` n `20`; unknown avg `-0.1951` n `793`
- 24h: commodity avg `0.3749` n `12`; crypto_alt avg `5.4967` n `230`; crypto_major avg `6.6153` n `8`; equity avg `-0.4376` n `121`; fx avg `-0.039` n `6`; index avg `-0.089` n `25`; metal avg `0.497` n `20`; unknown avg `2.5944` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
