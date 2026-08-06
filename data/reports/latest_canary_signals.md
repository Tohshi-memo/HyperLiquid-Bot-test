# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T01:52:26.824090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `12`; crypto_alt avg `-0.0393` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `0.1665` n `108`; fx avg `0.0088` n `6`; index avg `-0.0096` n `25`; metal avg `0.0534` n `20`; unknown avg `0.837` n `782`
- 1h: commodity avg `0.193` n `12`; crypto_alt avg `-0.2663` n `230`; crypto_major avg `-0.2656` n `8`; equity avg `-0.1252` n `108`; fx avg `-0.0021` n `6`; index avg `-0.0741` n `25`; metal avg `0.0369` n `20`; unknown avg `0.3878` n `782`
- 4h: commodity avg `0.0435` n `12`; crypto_alt avg `-0.0042` n `230`; crypto_major avg `-0.3017` n `8`; equity avg `-0.3818` n `108`; fx avg `-0.0625` n `6`; index avg `-0.187` n `25`; metal avg `0.2634` n `20`; unknown avg `0.0539` n `782`
- 24h: commodity avg `-0.0783` n `12`; crypto_alt avg `0.2153` n `230`; crypto_major avg `0.1888` n `8`; equity avg `-1.9847` n `108`; fx avg `-0.0289` n `6`; index avg `-0.3969` n `25`; metal avg `0.998` n `20`; unknown avg `1.0132` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
