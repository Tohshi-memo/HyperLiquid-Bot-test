# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T16:52:25.039653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0098` n `12`; crypto_alt avg `-0.115` n `230`; crypto_major avg `-0.0656` n `8`; equity avg `0.0048` n `114`; fx avg `-0.0044` n `6`; index avg `0.0001` n `25`; metal avg `0.0049` n `20`; unknown avg `0.2706` n `791`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `-0.0592` n `230`; crypto_major avg `0.1185` n `8`; equity avg `0.0276` n `114`; fx avg `0.0026` n `6`; index avg `0.0127` n `25`; metal avg `0.0119` n `20`; unknown avg `-0.0421` n `791`
- 4h: commodity avg `-0.0039` n `12`; crypto_alt avg `0.092` n `230`; crypto_major avg `0.3452` n `8`; equity avg `0.1423` n `114`; fx avg `0.0053` n `6`; index avg `0.0034` n `25`; metal avg `0.0104` n `20`; unknown avg `0.0896` n `791`
- 24h: commodity avg `0.0583` n `12`; crypto_alt avg `-0.2026` n `230`; crypto_major avg `0.0978` n `8`; equity avg `0.3552` n `114`; fx avg `-0.0068` n `6`; index avg `0.0373` n `25`; metal avg `0.055` n `20`; unknown avg `0.1842` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1847`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1582`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.155`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
