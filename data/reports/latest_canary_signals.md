# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T14:52:26.732134+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0653` n `12`; crypto_alt avg `-0.2895` n `228`; crypto_major avg `-0.3428` n `8`; equity avg `-0.4337` n `86`; fx avg `-0.0149` n `6`; index avg `-0.0403` n `23`; metal avg `0.0813` n `20`; unknown avg `-0.1328` n `764`
- 1h: commodity avg `-0.0477` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.0773` n `8`; equity avg `-0.0035` n `86`; fx avg `-0.0372` n `6`; index avg `0.0007` n `23`; metal avg `-0.1336` n `20`; unknown avg `-0.0152` n `764`
- 4h: commodity avg `-0.2459` n `12`; crypto_alt avg `0.8795` n `228`; crypto_major avg `0.4577` n `8`; equity avg `1.2768` n `86`; fx avg `-0.0912` n `6`; index avg `0.0779` n `23`; metal avg `-0.0357` n `20`; unknown avg `0.2819` n `764`
- 24h: commodity avg `-0.4541` n `12`; crypto_alt avg `-3.9553` n `228`; crypto_major avg `-4.4613` n `8`; equity avg `-2.9553` n `85`; fx avg `-0.1336` n `6`; index avg `-0.8807` n `23`; metal avg `-1.1915` n `20`; unknown avg `-0.1733` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
