# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T12:22:26.999173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0283` n `12`; crypto_alt avg `0.0327` n `232`; crypto_major avg `0.0409` n `8`; equity avg `0.0102` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0` n `26`; metal avg `-0.0059` n `20`; unknown avg `-0.0354` n `791`
- 1h: commodity avg `0.0587` n `12`; crypto_alt avg `0.1578` n `232`; crypto_major avg `0.1305` n `8`; equity avg `0.0131` n `134`; fx avg `0.001` n `6`; index avg `0.0021` n `26`; metal avg `-0.0023` n `20`; unknown avg `-0.0842` n `789`
- 4h: commodity avg `0.0442` n `12`; crypto_alt avg `0.3113` n `232`; crypto_major avg `0.3057` n `8`; equity avg `0.0996` n `134`; fx avg `-0.0151` n `6`; index avg `0.0264` n `26`; metal avg `-0.0091` n `20`; unknown avg `-0.1593` n `780`
- 24h: commodity avg `0.1826` n `12`; crypto_alt avg `0.6479` n `232`; crypto_major avg `-1.1427` n `8`; equity avg `0.8953` n `134`; fx avg `-0.0692` n `6`; index avg `0.0847` n `26`; metal avg `-0.1622` n `20`; unknown avg `17.0608` n `650`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
