# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T22:22:28.394746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `0.0211` n `230`; crypto_major avg `0.0704` n `8`; equity avg `0.0173` n `121`; fx avg `-0.0072` n `6`; index avg `-0.0033` n `25`; metal avg `0.0043` n `20`; unknown avg `-0.0493` n `793`
- 1h: commodity avg `-0.0052` n `12`; crypto_alt avg `0.2582` n `230`; crypto_major avg `-0.1863` n `8`; equity avg `-0.0033` n `121`; fx avg `-0.0208` n `6`; index avg `-0.0186` n `25`; metal avg `0.0051` n `20`; unknown avg `0.0275` n `793`
- 4h: commodity avg `0.0537` n `12`; crypto_alt avg `0.6711` n `230`; crypto_major avg `-0.1691` n `8`; equity avg `0.4851` n `121`; fx avg `-0.0396` n `6`; index avg `0.0273` n `25`; metal avg `0.0728` n `20`; unknown avg `-0.2352` n `792`
- 24h: commodity avg `0.3611` n `12`; crypto_alt avg `4.2245` n `230`; crypto_major avg `4.0669` n `8`; equity avg `-1.0366` n `121`; fx avg `0.1966` n `6`; index avg `-0.1389` n `25`; metal avg `0.0686` n `20`; unknown avg `2.6255` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
