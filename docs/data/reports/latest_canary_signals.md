# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T13:22:41.100989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1716` n `12`; crypto_alt avg `0.0136` n `228`; crypto_major avg `0.1456` n `8`; equity avg `0.1171` n `79`; fx avg `-0.0007` n `6`; index avg `0.0253` n `23`; metal avg `0.077` n `20`; unknown avg `-0.0252` n `722`
- 1h: commodity avg `-0.1301` n `12`; crypto_alt avg `0.0846` n `228`; crypto_major avg `0.3921` n `8`; equity avg `0.1439` n `79`; fx avg `-0.015` n `6`; index avg `0.0351` n `23`; metal avg `-0.0498` n `20`; unknown avg `-0.0273` n `722`
- 4h: commodity avg `-0.306` n `12`; crypto_alt avg `1.1475` n `228`; crypto_major avg `1.174` n `8`; equity avg `0.4856` n `79`; fx avg `0.0168` n `6`; index avg `0.1342` n `23`; metal avg `-0.0388` n `18`; unknown avg `0.8126` n `701`
- 24h: commodity avg `-0.4838` n `12`; crypto_alt avg `0.7183` n `228`; crypto_major avg `1.2832` n `8`; equity avg `0.329` n `79`; fx avg `0.1353` n `6`; index avg `0.1814` n `23`; metal avg `0.4787` n `18`; unknown avg `0.5854` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
