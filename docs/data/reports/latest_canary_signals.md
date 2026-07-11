# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T10:22:29.285127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0032` n `12`; crypto_alt avg `0.0442` n `230`; crypto_major avg `0.0438` n `8`; equity avg `-0.0106` n `92`; fx avg `-0.0029` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.034` n `765`
- 1h: commodity avg `-0.0162` n `12`; crypto_alt avg `-0.0603` n `230`; crypto_major avg `-0.1137` n `8`; equity avg `0.0048` n `92`; fx avg `-0.0054` n `6`; index avg `0.0038` n `25`; metal avg `-0.0021` n `20`; unknown avg `-0.0965` n `765`
- 4h: commodity avg `0.0678` n `12`; crypto_alt avg `-0.0589` n `230`; crypto_major avg `-0.0643` n `8`; equity avg `0.1117` n `92`; fx avg `-0.0165` n `6`; index avg `0.0279` n `25`; metal avg `-0.0007` n `20`; unknown avg `-0.0245` n `759`
- 24h: commodity avg `-0.188` n `12`; crypto_alt avg `-0.0004` n `229`; crypto_major avg `-0.7071` n `8`; equity avg `-0.112` n `92`; fx avg `-0.0872` n `6`; index avg `0.1374` n `25`; metal avg `0.1393` n `20`; unknown avg `2.938` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
