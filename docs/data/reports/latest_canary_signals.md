# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T10:22:25.251940+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0258` n `12`; crypto_alt avg `0.2753` n `232`; crypto_major avg `0.2572` n `8`; equity avg `0.084` n `130`; fx avg `-0.0008` n `6`; index avg `0.0296` n `26`; metal avg `0.121` n `20`; unknown avg `0.1791` n `792`
- 1h: commodity avg `-0.0446` n `12`; crypto_alt avg `0.2637` n `232`; crypto_major avg `0.1353` n `8`; equity avg `0.1705` n `130`; fx avg `0.0029` n `6`; index avg `0.0415` n `26`; metal avg `0.083` n `20`; unknown avg `-0.0905` n `790`
- 4h: commodity avg `0.1196` n `12`; crypto_alt avg `-0.9991` n `232`; crypto_major avg `-0.8874` n `8`; equity avg `-1.3495` n `130`; fx avg `0.0327` n `6`; index avg `-0.2702` n `26`; metal avg `-0.4884` n `20`; unknown avg `-0.11` n `788`
- 24h: commodity avg `0.2175` n `12`; crypto_alt avg `0.7014` n `232`; crypto_major avg `0.2333` n `8`; equity avg `-0.4971` n `130`; fx avg `0.0774` n `6`; index avg `-0.2292` n `26`; metal avg `-0.6403` n `20`; unknown avg `0.1154` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0309`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0295`, n `668`, weak_sample_signal
