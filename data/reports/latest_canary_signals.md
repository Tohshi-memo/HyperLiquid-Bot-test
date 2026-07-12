# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T18:52:27.254906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `0.0025` n `230`; crypto_major avg `0.0421` n `8`; equity avg `-0.0086` n `92`; fx avg `-0.0007` n `6`; index avg `0.0124` n `25`; metal avg `-0.0029` n `20`; unknown avg `-0.0269` n `765`
- 1h: commodity avg `0.0447` n `12`; crypto_alt avg `0.0225` n `230`; crypto_major avg `0.0961` n `8`; equity avg `0.0204` n `92`; fx avg `-0.1182` n `6`; index avg `-0.0186` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0396` n `765`
- 4h: commodity avg `0.1845` n `12`; crypto_alt avg `-0.118` n `230`; crypto_major avg `0.167` n `8`; equity avg `-0.0137` n `92`; fx avg `-0.0241` n `6`; index avg `0.0128` n `25`; metal avg `-0.0097` n `20`; unknown avg `-0.1061` n `759`
- 24h: commodity avg `0.5708` n `12`; crypto_alt avg `-1.3924` n `230`; crypto_major avg `-0.4876` n `8`; equity avg `-0.2193` n `92`; fx avg `-0.0041` n `6`; index avg `-0.0981` n `25`; metal avg `-0.1147` n `20`; unknown avg `0.1811` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
