# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-20T12:52:26.292404+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.113` n `12`; crypto_alt avg `0.1322` n `230`; crypto_major avg `0.1777` n `8`; equity avg `0.425` n `121`; fx avg `-0.0121` n `6`; index avg `0.0887` n `25`; metal avg `0.1341` n `20`; unknown avg `0.1142` n `792`
- 1h: commodity avg `-0.1314` n `12`; crypto_alt avg `-0.2331` n `230`; crypto_major avg `-0.1925` n `8`; equity avg `-0.2637` n `121`; fx avg `-0.0142` n `6`; index avg `-0.0327` n `25`; metal avg `0.0723` n `20`; unknown avg `-0.0298` n `792`
- 4h: commodity avg `0.0274` n `12`; crypto_alt avg `0.517` n `230`; crypto_major avg `0.3108` n `8`; equity avg `-0.7564` n `121`; fx avg `0.0055` n `6`; index avg `-0.1188` n `25`; metal avg `-0.0437` n `20`; unknown avg `0.5055` n `792`
- 24h: commodity avg `0.231` n `12`; crypto_alt avg `7.1725` n `230`; crypto_major avg `11.713` n `8`; equity avg `-1.6618` n `120`; fx avg `0.237` n `6`; index avg `-0.2529` n `25`; metal avg `0.4615` n `20`; unknown avg `2.7039` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
