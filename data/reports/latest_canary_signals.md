# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T14:37:25.518426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `12`; crypto_alt avg `0.207` n `232`; crypto_major avg `0.1894` n `8`; equity avg `0.0047` n `134`; fx avg `0.003` n `6`; index avg `0.0045` n `26`; metal avg `-0.0019` n `20`; unknown avg `-0.0592` n `794`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `0.1201` n `232`; crypto_major avg `0.0793` n `8`; equity avg `-0.0208` n `134`; fx avg `0.008` n `6`; index avg `-0.0078` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.1281` n `746`
- 4h: commodity avg `0.0638` n `12`; crypto_alt avg `0.3618` n `232`; crypto_major avg `0.8401` n `8`; equity avg `0.0358` n `134`; fx avg `0.0169` n `6`; index avg `0.0056` n `26`; metal avg `-0.0031` n `20`; unknown avg `-0.0923` n `728`
- 24h: commodity avg `0.1573` n `12`; crypto_alt avg `2.978` n `232`; crypto_major avg `2.0899` n `8`; equity avg `0.4965` n `134`; fx avg `0.0311` n `6`; index avg `0.0342` n `26`; metal avg `0.0088` n `20`; unknown avg `0.13` n `656`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1561`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
