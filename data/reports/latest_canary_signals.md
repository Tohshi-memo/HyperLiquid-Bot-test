# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T03:22:26.987364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0493` n `12`; crypto_alt avg `-0.237` n `232`; crypto_major avg `-0.1032` n `8`; equity avg `0.0136` n `133`; fx avg `-0.0083` n `6`; index avg `0.0002` n `26`; metal avg `-0.0014` n `20`; unknown avg `3.3794` n `793`
- 1h: commodity avg `0.0531` n `12`; crypto_alt avg `0.2881` n `232`; crypto_major avg `0.3385` n `8`; equity avg `0.0904` n `133`; fx avg `-0.0102` n `6`; index avg `0.0154` n `26`; metal avg `-0.0274` n `20`; unknown avg `3.7837` n `791`
- 4h: commodity avg `0.0095` n `12`; crypto_alt avg `-0.0635` n `232`; crypto_major avg `-0.0387` n `8`; equity avg `0.3939` n `133`; fx avg `0.0123` n `6`; index avg `0.0413` n `26`; metal avg `-0.0822` n `20`; unknown avg `1.064` n `784`
- 24h: commodity avg `-0.1148` n `12`; crypto_alt avg `2.8213` n `232`; crypto_major avg `4.1455` n `8`; equity avg `1.3673` n `133`; fx avg `-0.1129` n `6`; index avg `0.1899` n `26`; metal avg `0.4882` n `20`; unknown avg `3.7211` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
