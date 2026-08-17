# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T19:13:00.754043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0196` n `12`; crypto_alt avg `-0.1232` n `230`; crypto_major avg `-0.1785` n `8`; equity avg `-0.2653` n `114`; fx avg `0.0106` n `6`; index avg `-0.0314` n `25`; metal avg `-0.0152` n `20`; unknown avg `0.0608` n `792`
- 1h: commodity avg `0.0065` n `12`; crypto_alt avg `-0.0102` n `230`; crypto_major avg `-0.1053` n `8`; equity avg `-0.2324` n `114`; fx avg `0.0004` n `6`; index avg `-0.0457` n `25`; metal avg `-0.0786` n `20`; unknown avg `-0.0734` n `792`
- 4h: commodity avg `0.4306` n `12`; crypto_alt avg `-0.11` n `230`; crypto_major avg `-0.1149` n `8`; equity avg `-0.4684` n `114`; fx avg `0.0317` n `6`; index avg `-0.1544` n `25`; metal avg `-0.1466` n `20`; unknown avg `0.0745` n `792`
- 24h: commodity avg `0.3032` n `12`; crypto_alt avg `-0.0657` n `230`; crypto_major avg `0.7691` n `8`; equity avg `1.094` n `114`; fx avg `0.0228` n `6`; index avg `0.0715` n `25`; metal avg `0.1415` n `20`; unknown avg `0.1887` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1648`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1338`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
