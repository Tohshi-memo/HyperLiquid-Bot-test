# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T08:07:28.635376+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0534` n `12`; crypto_alt avg `-0.0311` n `228`; crypto_major avg `-0.1264` n `8`; equity avg `0.0158` n `74`; fx avg `0.0061` n `6`; index avg `0.0213` n `23`; metal avg `-0.002` n `18`; unknown avg `-0.2207` n `643`
- 1h: commodity avg `-0.0487` n `12`; crypto_alt avg `0.6754` n `228`; crypto_major avg `0.2936` n `8`; equity avg `0.193` n `74`; fx avg `0.0035` n `6`; index avg `-0.0027` n `23`; metal avg `0.0586` n `18`; unknown avg `0.3645` n `643`
- 4h: commodity avg `-0.0982` n `12`; crypto_alt avg `1.146` n `228`; crypto_major avg `0.5201` n `8`; equity avg `0.1387` n `74`; fx avg `0.0045` n `6`; index avg `0.0099` n `23`; metal avg `0.0811` n `18`; unknown avg `-0.2117` n `619`
- 24h: commodity avg `-0.0625` n `12`; crypto_alt avg `1.416` n `228`; crypto_major avg `0.6381` n `8`; equity avg `-0.1662` n `74`; fx avg `0.0311` n `6`; index avg `0.795` n `23`; metal avg `0.6628` n `18`; unknown avg `27.6912` n `619`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
