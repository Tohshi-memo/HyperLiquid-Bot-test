# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T13:22:35.759987+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0812` n `12`; crypto_alt avg `-0.3937` n `234`; crypto_major avg `-0.4074` n `8`; equity avg `-0.098` n `141`; fx avg `-0.0444` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0585` n `20`; unknown avg `1.3348` n `944`
- 1h: commodity avg `-0.0744` n `12`; crypto_alt avg `0.4213` n `234`; crypto_major avg `0.1068` n `8`; equity avg `-0.041` n `141`; fx avg `-0.0525` n `6`; index avg `-0.0326` n `26`; metal avg `-0.1547` n `20`; unknown avg `34.777` n `942`
- 4h: commodity avg `-0.1079` n `12`; crypto_alt avg `0.8826` n `234`; crypto_major avg `0.7461` n `8`; equity avg `-0.2006` n `141`; fx avg `-0.0332` n `6`; index avg `-0.043` n `26`; metal avg `-0.0423` n `20`; unknown avg `2.9284` n `936`
- 24h: commodity avg `0.0008` n `12`; crypto_alt avg `4.1457` n `234`; crypto_major avg `2.5117` n `8`; equity avg `1.673` n `141`; fx avg `-0.2307` n `6`; index avg `0.2234` n `26`; metal avg `0.0704` n `20`; unknown avg `12.1798` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
