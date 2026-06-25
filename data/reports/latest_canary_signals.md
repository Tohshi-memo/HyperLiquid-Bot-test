# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T04:07:39.521582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0085` n `12`; crypto_alt avg `-0.0473` n `228`; crypto_major avg `0.0199` n `8`; equity avg `0.0476` n `86`; fx avg `0.0223` n `6`; index avg `0.0228` n `23`; metal avg `0.0065` n `20`; unknown avg `0.0382` n `765`
- 1h: commodity avg `0.0451` n `12`; crypto_alt avg `-0.0643` n `228`; crypto_major avg `-0.1148` n `8`; equity avg `0.0508` n `86`; fx avg `0.0368` n `6`; index avg `0.006` n `23`; metal avg `0.2649` n `20`; unknown avg `-0.3771` n `764`
- 4h: commodity avg `-0.1265` n `12`; crypto_alt avg `-0.3887` n `228`; crypto_major avg `-0.4426` n `8`; equity avg `-0.4843` n `86`; fx avg `0.0505` n `6`; index avg `0.077` n `23`; metal avg `-0.1143` n `20`; unknown avg `0.1594` n `748`
- 24h: commodity avg `-0.4751` n `12`; crypto_alt avg `-1.9018` n `228`; crypto_major avg `-1.7605` n `8`; equity avg `0.2599` n `86`; fx avg `0.095` n `6`; index avg `0.6919` n `23`; metal avg `-1.3176` n `20`; unknown avg `-0.5625` n `700`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
