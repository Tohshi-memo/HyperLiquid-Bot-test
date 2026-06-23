# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T22:37:30.346503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `-0.2683` n `228`; crypto_major avg `-0.1478` n `8`; equity avg `-0.1936` n `86`; fx avg `-0.0053` n `6`; index avg `-0.0488` n `23`; metal avg `-0.0279` n `20`; unknown avg `-0.1047` n `764`
- 1h: commodity avg `-0.0128` n `12`; crypto_alt avg `-0.1433` n `228`; crypto_major avg `-0.0411` n `8`; equity avg `-0.1536` n `86`; fx avg `-0.0213` n `6`; index avg `-0.0135` n `23`; metal avg `-0.1281` n `20`; unknown avg `-0.5259` n `764`
- 4h: commodity avg `-0.0137` n `12`; crypto_alt avg `0.515` n `228`; crypto_major avg `0.3701` n `8`; equity avg `-0.1137` n `86`; fx avg `-0.0119` n `6`; index avg `0.0325` n `23`; metal avg `-0.1205` n `20`; unknown avg `1.1524` n `756`
- 24h: commodity avg `-0.472` n `12`; crypto_alt avg `-1.598` n `228`; crypto_major avg `-2.8286` n `8`; equity avg `-3.2183` n `86`; fx avg `-0.186` n `6`; index avg `-0.8882` n `23`; metal avg `-1.2692` n `20`; unknown avg `1.7867` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
