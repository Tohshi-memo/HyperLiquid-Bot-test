# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T01:37:25.676564+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0863` n `12`; crypto_alt avg `0.079` n `228`; crypto_major avg `0.0401` n `8`; equity avg `0.0574` n `86`; fx avg `-0.0094` n `6`; index avg `0.0529` n `23`; metal avg `-0.2076` n `20`; unknown avg `-0.056` n `764`
- 1h: commodity avg `-0.1897` n `12`; crypto_alt avg `0.0616` n `228`; crypto_major avg `-0.0266` n `8`; equity avg `-0.1712` n `86`; fx avg `0.0052` n `6`; index avg `0.0124` n `23`; metal avg `-0.1659` n `20`; unknown avg `-0.1991` n `764`
- 4h: commodity avg `-0.1091` n `12`; crypto_alt avg `0.1754` n `228`; crypto_major avg `0.1579` n `8`; equity avg `-0.0712` n `86`; fx avg `0.0685` n `6`; index avg `-0.0305` n `23`; metal avg `-0.3139` n `20`; unknown avg `-0.8231` n `748`
- 24h: commodity avg `-0.6028` n `12`; crypto_alt avg `-2.7805` n `228`; crypto_major avg `-2.6264` n `8`; equity avg `3.8052` n `86`; fx avg `0.086` n `6`; index avg `0.4349` n `23`; metal avg `-1.8671` n `20`; unknown avg `-1.2693` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
