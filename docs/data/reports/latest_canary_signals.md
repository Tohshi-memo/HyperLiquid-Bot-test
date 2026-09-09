# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T00:37:25.075145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0126` n `12`; crypto_alt avg `-0.2424` n `233`; crypto_major avg `-0.0645` n `8`; equity avg `-0.1572` n `134`; fx avg `0.0338` n `6`; index avg `-0.0341` n `26`; metal avg `0.0181` n `20`; unknown avg `0.1331` n `791`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.0644` n `233`; crypto_major avg `0.272` n `8`; equity avg `0.0566` n `134`; fx avg `0.0102` n `6`; index avg `0.0242` n `26`; metal avg `-0.0143` n `20`; unknown avg `-0.0625` n `789`
- 4h: commodity avg `0.0345` n `12`; crypto_alt avg `0.0915` n `233`; crypto_major avg `0.4991` n `8`; equity avg `0.0144` n `134`; fx avg `-0.0215` n `6`; index avg `0.0233` n `26`; metal avg `-0.0129` n `20`; unknown avg `1.0394` n `741`
- 24h: commodity avg `0.1489` n `12`; crypto_alt avg `-0.5564` n `232`; crypto_major avg `0.2659` n `8`; equity avg `0.1382` n `134`; fx avg `-0.0068` n `6`; index avg `-0.1691` n `26`; metal avg `-0.4532` n `20`; unknown avg `0.8302` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
