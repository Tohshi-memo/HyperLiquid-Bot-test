# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T20:52:34.711849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0593` n `12`; crypto_alt avg `-0.3937` n `228`; crypto_major avg `-0.311` n `8`; equity avg `-0.0505` n `74`; fx avg `0.0245` n `6`; index avg `-0.0081` n `23`; metal avg `0.0319` n `18`; unknown avg `0.8293` n `643`
- 1h: commodity avg `-0.0601` n `12`; crypto_alt avg `-0.1838` n `228`; crypto_major avg `-0.1272` n `8`; equity avg `0.0438` n `74`; fx avg `0.0165` n `6`; index avg `0.1554` n `23`; metal avg `0.2379` n `18`; unknown avg `0.5294` n `643`
- 4h: commodity avg `-0.1178` n `12`; crypto_alt avg `-0.8234` n `228`; crypto_major avg `-0.8108` n `8`; equity avg `-0.4123` n `74`; fx avg `0.01` n `6`; index avg `0.0012` n `23`; metal avg `0.2504` n `18`; unknown avg `0.1133` n `643`
- 24h: commodity avg `-0.6955` n `12`; crypto_alt avg `-0.2712` n `228`; crypto_major avg `0.5965` n `8`; equity avg `-0.1965` n `74`; fx avg `0.03` n `6`; index avg `0.5921` n `23`; metal avg `0.6` n `18`; unknown avg `40.6606` n `514`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
