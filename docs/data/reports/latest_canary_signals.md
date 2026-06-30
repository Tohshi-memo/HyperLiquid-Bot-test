# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T19:15:04.427817+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.25` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `-0.1686` n `228`; crypto_major avg `-0.1024` n `8`; equity avg `0.1463` n `88`; fx avg `-0.0035` n `6`; index avg `0.0086` n `23`; metal avg `0.0005` n `20`; unknown avg `-0.1272` n `765`
- 1h: commodity avg `0.087` n `12`; crypto_alt avg `-0.1386` n `228`; crypto_major avg `0.0081` n `8`; equity avg `0.1492` n `88`; fx avg `-0.0006` n `6`; index avg `0.0144` n `23`; metal avg `-0.0002` n `20`; unknown avg `-0.3905` n `765`
- 4h: commodity avg `-0.2322` n `12`; crypto_alt avg `0.2802` n `228`; crypto_major avg `0.7744` n `8`; equity avg `0.767` n `88`; fx avg `-0.0368` n `6`; index avg `0.1041` n `23`; metal avg `0.0571` n `20`; unknown avg `-0.1572` n `765`
- 24h: commodity avg `0.1055` n `12`; crypto_alt avg `-2.3968` n `228`; crypto_major avg `-2.2834` n `8`; equity avg `1.1801` n `88`; fx avg `0.1404` n `6`; index avg `0.3181` n `23`; metal avg `0.275` n `20`; unknown avg `7.9978` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0522`, n `668`, weak_sample_signal
