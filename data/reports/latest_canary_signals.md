# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T10:22:27.388908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0432` n `12`; crypto_alt avg `-0.0133` n `228`; crypto_major avg `-0.0945` n `8`; equity avg `-0.0785` n `86`; fx avg `0.015` n `6`; index avg `-0.0071` n `23`; metal avg `-0.0448` n `20`; unknown avg `-0.0379` n `765`
- 1h: commodity avg `0.0014` n `12`; crypto_alt avg `-0.5819` n `228`; crypto_major avg `-0.7056` n `8`; equity avg `-0.1066` n `86`; fx avg `0.0221` n `6`; index avg `0.0002` n `23`; metal avg `0.0009` n `20`; unknown avg `-0.116` n `765`
- 4h: commodity avg `-0.3163` n `12`; crypto_alt avg `-0.0416` n `228`; crypto_major avg `-0.4145` n `8`; equity avg `-0.0636` n `86`; fx avg `0.0759` n `6`; index avg `0.0005` n `23`; metal avg `0.3948` n `20`; unknown avg `-0.0429` n `757`
- 24h: commodity avg `0.0021` n `12`; crypto_alt avg `-1.9906` n `228`; crypto_major avg `-2.2793` n `8`; equity avg `-4.2799` n `86`; fx avg `0.0519` n `6`; index avg `-0.6095` n `23`; metal avg `0.5569` n `20`; unknown avg `0.6762` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2719`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2037`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
