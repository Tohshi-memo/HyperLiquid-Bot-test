# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T23:42:09.913879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `-0.0158` n `228`; crypto_major avg `0.0752` n `8`; equity avg `0.0358` n `86`; fx avg `0.0251` n `6`; index avg `-0.0054` n `23`; metal avg `0.0135` n `20`; unknown avg `-0.041` n `716`
- 1h: commodity avg `-0.0527` n `12`; crypto_alt avg `0.2928` n `228`; crypto_major avg `0.2593` n `8`; equity avg `-0.067` n `86`; fx avg `0.0388` n `6`; index avg `-0.0143` n `23`; metal avg `0.0215` n `20`; unknown avg `0.1373` n `716`
- 4h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.8709` n `228`; crypto_major avg `-0.6643` n `8`; equity avg `-0.1011` n `86`; fx avg `0.0298` n `6`; index avg `-0.0089` n `23`; metal avg `0.0364` n `20`; unknown avg `-0.1887` n `708`
- 24h: commodity avg `-0.9146` n `12`; crypto_alt avg `0.0641` n `228`; crypto_major avg `0.4546` n `8`; equity avg `-0.1957` n `85`; fx avg `0.1342` n `6`; index avg `0.2244` n `23`; metal avg `0.4649` n `18`; unknown avg `0.4475` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
