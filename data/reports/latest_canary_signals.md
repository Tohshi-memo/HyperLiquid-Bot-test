# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T12:22:29.878667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0385` n `12`; crypto_alt avg `-0.1222` n `228`; crypto_major avg `-0.0749` n `8`; equity avg `0.0275` n `86`; fx avg `-0.0073` n `6`; index avg `0.0225` n `23`; metal avg `-0.033` n `20`; unknown avg `-0.0032` n `764`
- 1h: commodity avg `-0.1855` n `12`; crypto_alt avg `0.9346` n `228`; crypto_major avg `0.9` n `8`; equity avg `0.3352` n `86`; fx avg `-0.0201` n `6`; index avg `0.1004` n `23`; metal avg `-0.1734` n `20`; unknown avg `0.329` n `764`
- 4h: commodity avg `-0.1395` n `12`; crypto_alt avg `0.1223` n `228`; crypto_major avg `0.1736` n `8`; equity avg `-0.0128` n `86`; fx avg `-0.0416` n `6`; index avg `0.0784` n `23`; metal avg `-0.7824` n `20`; unknown avg `-0.114` n `764`
- 24h: commodity avg `-0.5958` n `12`; crypto_alt avg `0.0529` n `228`; crypto_major avg `0.1063` n `8`; equity avg `4.7967` n `86`; fx avg `-0.008` n `6`; index avg `0.2229` n `23`; metal avg `-1.0392` n `20`; unknown avg `-0.1322` n `716`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
