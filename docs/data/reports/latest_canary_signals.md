# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T17:51:43.008563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `-0.0093` n `230`; crypto_major avg `0.0981` n `8`; equity avg `0.0039` n `114`; fx avg `-0.0004` n `6`; index avg `-0.0001` n `25`; metal avg `0.0261` n `20`; unknown avg `-0.0546` n `792`
- 1h: commodity avg `0.281` n `12`; crypto_alt avg `-0.0838` n `230`; crypto_major avg `-0.0575` n `8`; equity avg `-0.3021` n `114`; fx avg `0.0105` n `6`; index avg `-0.0619` n `25`; metal avg `-0.0391` n `20`; unknown avg `0.0908` n `792`
- 4h: commodity avg `0.3467` n `12`; crypto_alt avg `-0.0546` n `230`; crypto_major avg `0.2068` n `8`; equity avg `0.2708` n `114`; fx avg `0.0271` n `6`; index avg `-0.0458` n `25`; metal avg `0.0329` n `20`; unknown avg `0.1633` n `792`
- 24h: commodity avg `0.327` n `12`; crypto_alt avg `-0.1534` n `230`; crypto_major avg `0.8093` n `8`; equity avg `1.3517` n `114`; fx avg `0.0255` n `6`; index avg `0.1296` n `25`; metal avg `0.2203` n `20`; unknown avg `0.2149` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
