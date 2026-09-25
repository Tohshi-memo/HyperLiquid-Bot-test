# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T10:37:32.456718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `0.2722` n `234`; crypto_major avg `0.4246` n `8`; equity avg `-0.0116` n `141`; fx avg `-0.0082` n `6`; index avg `-0.0203` n `26`; metal avg `-0.0157` n `20`; unknown avg `1.3927` n `946`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.1319` n `234`; crypto_major avg `0.0514` n `8`; equity avg `-0.0957` n `141`; fx avg `-0.0016` n `6`; index avg `-0.0244` n `26`; metal avg `0.1055` n `20`; unknown avg `1.0333` n `944`
- 4h: commodity avg `-0.0444` n `12`; crypto_alt avg `1.8644` n `234`; crypto_major avg `1.4617` n `8`; equity avg `0.2197` n `141`; fx avg `-0.0318` n `6`; index avg `0.0285` n `26`; metal avg `0.2533` n `20`; unknown avg `3.3621` n `926`
- 24h: commodity avg `0.0553` n `12`; crypto_alt avg `5.6654` n `234`; crypto_major avg `3.5083` n `8`; equity avg `1.9231` n `141`; fx avg `-0.2363` n `6`; index avg `0.3008` n `26`; metal avg `0.2976` n `20`; unknown avg `12.9731` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
