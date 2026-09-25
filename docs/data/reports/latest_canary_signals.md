# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T23:22:32.208087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0133` n `12`; crypto_alt avg `0.2094` n `234`; crypto_major avg `0.0337` n `8`; equity avg `-0.0067` n `141`; fx avg `-0.0031` n `6`; index avg `0.0086` n `26`; metal avg `0.0058` n `20`; unknown avg `0.1806` n `960`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.7066` n `234`; crypto_major avg `0.3138` n `8`; equity avg `0.0126` n `141`; fx avg `0.0046` n `6`; index avg `0.011` n `26`; metal avg `0.0091` n `20`; unknown avg `0.4939` n `958`
- 4h: commodity avg `0.0328` n `12`; crypto_alt avg `0.9025` n `234`; crypto_major avg `0.3456` n `8`; equity avg `-0.0116` n `141`; fx avg `-0.0122` n `6`; index avg `0.0351` n `26`; metal avg `-0.0174` n `20`; unknown avg `0.129` n `852`
- 24h: commodity avg `-0.3793` n `12`; crypto_alt avg `3.1833` n `234`; crypto_major avg `1.3219` n `8`; equity avg `0.1497` n `141`; fx avg `-0.2691` n `6`; index avg `0.2793` n `26`; metal avg `0.1621` n `20`; unknown avg `1124.9405` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1453`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
