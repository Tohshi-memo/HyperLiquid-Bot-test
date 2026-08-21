# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T14:49:53.781073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0236` n `12`; crypto_alt avg `0.2238` n `230`; crypto_major avg `0.1516` n `8`; equity avg `0.0671` n `121`; fx avg `0.0083` n `6`; index avg `0.0124` n `25`; metal avg `-0.0039` n `20`; unknown avg `0.0042` n `793`
- 1h: commodity avg `0.033` n `12`; crypto_alt avg `0.3592` n `230`; crypto_major avg `0.0243` n `8`; equity avg `-0.5411` n `121`; fx avg `-0.0021` n `6`; index avg `-0.029` n `25`; metal avg `-0.0615` n `20`; unknown avg `-0.0389` n `793`
- 4h: commodity avg `-0.055` n `12`; crypto_alt avg `1.3502` n `230`; crypto_major avg `0.4288` n `8`; equity avg `-0.7798` n `121`; fx avg `-0.0191` n `6`; index avg `-0.0965` n `25`; metal avg `-0.05` n `20`; unknown avg `0.1888` n `793`
- 24h: commodity avg `0.2745` n `12`; crypto_alt avg `8.5729` n `230`; crypto_major avg `6.6691` n `8`; equity avg `0.6758` n `121`; fx avg `-0.0851` n `6`; index avg `-0.0101` n `25`; metal avg `0.6114` n `20`; unknown avg `3.2278` n `776`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2355`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
