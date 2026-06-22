# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T22:00:22.224806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `0.0501` n `228`; crypto_major avg `0.1499` n `8`; equity avg `0.0014` n `86`; fx avg `0.0003` n `6`; index avg `-0.0061` n `23`; metal avg `0.0153` n `20`; unknown avg `0.0196` n `716`
- 1h: commodity avg `0.0045` n `12`; crypto_alt avg `-0.2861` n `228`; crypto_major avg `-0.1533` n `8`; equity avg `-0.0172` n `86`; fx avg `-0.0409` n `6`; index avg `0.0118` n `23`; metal avg `0.0215` n `20`; unknown avg `-0.2931` n `716`
- 4h: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.9146` n `228`; crypto_major avg `-0.7282` n `8`; equity avg `-0.3265` n `86`; fx avg `-0.0263` n `6`; index avg `-0.0487` n `23`; metal avg `0.0979` n `20`; unknown avg `-0.2109` n `708`
- 24h: commodity avg `-0.9333` n `12`; crypto_alt avg `0.0056` n `228`; crypto_major avg `0.3667` n `8`; equity avg `-0.4534` n `85`; fx avg `0.0645` n `6`; index avg `0.1719` n `23`; metal avg `0.4256` n `18`; unknown avg `0.4178` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
