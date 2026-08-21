# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T06:37:29.113700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0345` n `12`; crypto_alt avg `-0.0679` n `230`; crypto_major avg `-0.1444` n `8`; equity avg `0.1913` n `121`; fx avg `0.0087` n `6`; index avg `0.0213` n `25`; metal avg `0.0671` n `20`; unknown avg `-0.034` n `793`
- 1h: commodity avg `0.0376` n `12`; crypto_alt avg `0.3755` n `230`; crypto_major avg `0.3696` n `8`; equity avg `0.1261` n `121`; fx avg `0.0509` n `6`; index avg `0.0176` n `25`; metal avg `0.1176` n `20`; unknown avg `-0.1034` n `777`
- 4h: commodity avg `-0.0735` n `12`; crypto_alt avg `1.1219` n `230`; crypto_major avg `0.4908` n `8`; equity avg `-0.0485` n `121`; fx avg `0.0566` n `6`; index avg `0.0153` n `25`; metal avg `0.1488` n `20`; unknown avg `-0.0662` n `777`
- 24h: commodity avg `0.3174` n `12`; crypto_alt avg `6.2309` n `230`; crypto_major avg `7.0041` n `8`; equity avg `-0.3778` n `121`; fx avg `0.0458` n `6`; index avg `-0.0835` n `25`; metal avg `0.6431` n `20`; unknown avg `2.4074` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1925`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
