# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T19:07:31.028328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `0.1898` n `228`; crypto_major avg `0.1169` n `8`; equity avg `0.2229` n `86`; fx avg `-0.0034` n `6`; index avg `0.0678` n `23`; metal avg `0.1077` n `20`; unknown avg `-0.066` n `764`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `0.4561` n `228`; crypto_major avg `0.2401` n `8`; equity avg `-0.188` n `86`; fx avg `-0.0011` n `6`; index avg `0.0117` n `23`; metal avg `-0.0276` n `20`; unknown avg `-0.1682` n `764`
- 4h: commodity avg `-0.1104` n `12`; crypto_alt avg `-0.0003` n `228`; crypto_major avg `-0.0247` n `8`; equity avg `-0.5808` n `86`; fx avg `-0.0238` n `6`; index avg `-0.0865` n `23`; metal avg `-0.1154` n `20`; unknown avg `-0.6901` n `764`
- 24h: commodity avg `-0.3989` n `12`; crypto_alt avg `-3.0407` n `228`; crypto_major avg `-3.9016` n `8`; equity avg `-3.3529` n `86`; fx avg `-0.171` n `6`; index avg `-0.8867` n `23`; metal avg `-1.1588` n `20`; unknown avg `-0.4385` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
