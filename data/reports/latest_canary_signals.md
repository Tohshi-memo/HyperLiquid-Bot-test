# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T05:50:33.523947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.1622` n `230`; crypto_major avg `0.154` n `8`; equity avg `0.061` n `114`; fx avg `0.0019` n `6`; index avg `-0.0073` n `25`; metal avg `0.0623` n `20`; unknown avg `-0.1283` n `793`
- 1h: commodity avg `-0.0579` n `12`; crypto_alt avg `-0.0664` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `-0.2504` n `114`; fx avg `-0.0309` n `6`; index avg `-0.0755` n `25`; metal avg `0.0071` n `20`; unknown avg `-0.2647` n `793`
- 4h: commodity avg `-0.029` n `12`; crypto_alt avg `-0.653` n `230`; crypto_major avg `-0.1452` n `8`; equity avg `-0.843` n `114`; fx avg `0.0096` n `6`; index avg `-0.2206` n `25`; metal avg `-0.0735` n `20`; unknown avg `-0.0329` n `793`
- 24h: commodity avg `0.6731` n `12`; crypto_alt avg `-1.3948` n `230`; crypto_major avg `0.0184` n `8`; equity avg `-1.473` n `114`; fx avg `-0.0235` n `6`; index avg `-0.3962` n `25`; metal avg `-0.222` n `20`; unknown avg `0.1037` n `776`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1556`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
