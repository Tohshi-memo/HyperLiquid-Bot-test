# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T02:52:28.663797+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0503` n `12`; crypto_alt avg `-0.0619` n `230`; crypto_major avg `-0.1217` n `8`; equity avg `-0.0456` n `121`; fx avg `0.0127` n `6`; index avg `-0.0316` n `25`; metal avg `0.0028` n `20`; unknown avg `0.1394` n `792`
- 1h: commodity avg `-0.0118` n `12`; crypto_alt avg `-0.3117` n `230`; crypto_major avg `-0.3277` n `8`; equity avg `-0.2199` n `121`; fx avg `-0.0068` n `6`; index avg `-0.0515` n `25`; metal avg `0.0591` n `20`; unknown avg `0.1548` n `792`
- 4h: commodity avg `0.1109` n `12`; crypto_alt avg `0.3614` n `230`; crypto_major avg `-0.0021` n `8`; equity avg `0.0205` n `121`; fx avg `0.0879` n `6`; index avg `0.0504` n `25`; metal avg `-0.1579` n `20`; unknown avg `0.008` n `792`
- 24h: commodity avg `-0.0638` n `12`; crypto_alt avg `5.6441` n `230`; crypto_major avg `9.8084` n `8`; equity avg `0.8641` n `120`; fx avg `0.0357` n `6`; index avg `0.273` n `25`; metal avg `1.0116` n `20`; unknown avg `1.6226` n `757`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
