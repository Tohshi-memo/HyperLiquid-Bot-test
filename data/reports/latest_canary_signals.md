# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T17:19:36.851827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0502` n `12`; crypto_alt avg `0.1337` n `230`; crypto_major avg `0.0873` n `8`; equity avg `-0.1342` n `114`; fx avg `0.0066` n `6`; index avg `-0.0212` n `25`; metal avg `-0.0289` n `20`; unknown avg `0.1242` n `792`
- 1h: commodity avg `0.2147` n `12`; crypto_alt avg `0.0652` n `230`; crypto_major avg `-0.0203` n `8`; equity avg `-0.1164` n `114`; fx avg `0.0142` n `6`; index avg `-0.0633` n `25`; metal avg `-0.0718` n `20`; unknown avg `0.2339` n `792`
- 4h: commodity avg `0.1939` n `12`; crypto_alt avg `0.2665` n `230`; crypto_major avg `0.593` n `8`; equity avg `0.7323` n `114`; fx avg `0.0138` n `6`; index avg `0.0418` n `25`; metal avg `0.2094` n `20`; unknown avg `0.3015` n `792`
- 24h: commodity avg `0.195` n `12`; crypto_alt avg `-0.02` n `230`; crypto_major avg `0.7704` n `8`; equity avg `1.5265` n `114`; fx avg `0.022` n `6`; index avg `0.1537` n `25`; metal avg `0.2393` n `20`; unknown avg `0.2496` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1565`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
