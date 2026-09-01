# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T07:22:32.631883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0782` n `12`; crypto_alt avg `0.1293` n `232`; crypto_major avg `0.0162` n `8`; equity avg `0.0148` n `130`; fx avg `0.0163` n `6`; index avg `0.0052` n `26`; metal avg `0.0308` n `20`; unknown avg `0.0261` n `792`
- 1h: commodity avg `0.1037` n `12`; crypto_alt avg `0.164` n `232`; crypto_major avg `-0.0792` n `8`; equity avg `-0.0559` n `130`; fx avg `0.0293` n `6`; index avg `0.0008` n `26`; metal avg `0.0104` n `20`; unknown avg `0.042` n `788`
- 4h: commodity avg `0.1379` n `12`; crypto_alt avg `0.6372` n `232`; crypto_major avg `0.2853` n `8`; equity avg `0.3326` n `130`; fx avg `0.0315` n `6`; index avg `0.0645` n `26`; metal avg `0.0398` n `20`; unknown avg `0.0956` n `770`
- 24h: commodity avg `0.6586` n `12`; crypto_alt avg `1.4808` n `232`; crypto_major avg `1.1348` n `8`; equity avg `0.4755` n `130`; fx avg `0.0658` n `6`; index avg `-0.002` n `26`; metal avg `-0.1879` n `20`; unknown avg `0.2092` n `749`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0548`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
