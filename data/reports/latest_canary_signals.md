# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T07:22:26.248227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `0.0069` n `228`; crypto_major avg `0.0897` n `8`; equity avg `0.0017` n `86`; fx avg `-0.0173` n `6`; index avg `0.0004` n `23`; metal avg `0.0142` n `20`; unknown avg `-0.0085` n `764`
- 1h: commodity avg `-0.0583` n `12`; crypto_alt avg `-0.0842` n `228`; crypto_major avg `-0.1908` n `8`; equity avg `-0.144` n `86`; fx avg `0.0198` n `6`; index avg `0.0008` n `23`; metal avg `-0.1067` n `20`; unknown avg `-0.1748` n `756`
- 4h: commodity avg `0.0049` n `12`; crypto_alt avg `0.1718` n `228`; crypto_major avg `0.5669` n `8`; equity avg `0.6131` n `86`; fx avg `0.0738` n `6`; index avg `0.2489` n `23`; metal avg `0.304` n `20`; unknown avg `-0.0495` n `732`
- 24h: commodity avg `-0.299` n `12`; crypto_alt avg `-0.9229` n `228`; crypto_major avg `-1.3134` n `8`; equity avg `4.2033` n `86`; fx avg `-0.0596` n `6`; index avg `0.0134` n `23`; metal avg `-0.3511` n `20`; unknown avg `0.0309` n `572`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
