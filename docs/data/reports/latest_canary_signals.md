# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T05:46:00.500301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0087` n `12`; crypto_alt avg `-0.0241` n `230`; crypto_major avg `0.0466` n `8`; equity avg `-0.0925` n `121`; fx avg `0.0118` n `6`; index avg `-0.0118` n `25`; metal avg `0.0129` n `20`; unknown avg `0.01` n `793`
- 1h: commodity avg `0.0089` n `12`; crypto_alt avg `0.2216` n `230`; crypto_major avg `0.2306` n `8`; equity avg `0.0269` n `121`; fx avg `0.0163` n `6`; index avg `-0.0068` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.16` n `793`
- 4h: commodity avg `-0.0876` n `12`; crypto_alt avg `0.799` n `230`; crypto_major avg `-0.1562` n `8`; equity avg `0.0905` n `121`; fx avg `0.0208` n `6`; index avg `0.0437` n `25`; metal avg `0.1237` n `20`; unknown avg `-0.086` n `793`
- 24h: commodity avg `0.2591` n `12`; crypto_alt avg `6.2468` n `230`; crypto_major avg `7.2365` n `8`; equity avg `-0.3787` n `121`; fx avg `-0.0343` n `6`; index avg `-0.0587` n `25`; metal avg `0.6484` n `20`; unknown avg `2.7196` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1824`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
