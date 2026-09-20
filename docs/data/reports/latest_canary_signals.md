# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T00:22:25.837918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.143` n `234`; crypto_major avg `-0.022` n `8`; equity avg `0.0068` n `140`; fx avg `0.0011` n `6`; index avg `-0.0013` n `26`; metal avg `0.0048` n `20`; unknown avg `0.1657` n `943`
- 1h: commodity avg `0.0711` n `12`; crypto_alt avg `0.2886` n `234`; crypto_major avg `-0.1111` n `8`; equity avg `0.0347` n `140`; fx avg `0.006` n `6`; index avg `0.001` n `26`; metal avg `0.0132` n `20`; unknown avg `0.1576` n `919`
- 4h: commodity avg `0.1437` n `12`; crypto_alt avg `-0.1085` n `234`; crypto_major avg `-0.5791` n `8`; equity avg `0.0038` n `140`; fx avg `-0.0029` n `6`; index avg `0.0021` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.6068` n `911`
- 24h: commodity avg `0.0132` n `12`; crypto_alt avg `0.9689` n `234`; crypto_major avg `-0.3043` n `8`; equity avg `-0.0519` n `140`; fx avg `-0.0672` n `6`; index avg `0.0085` n `26`; metal avg `-0.0143` n `20`; unknown avg `0.7543` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1525`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
