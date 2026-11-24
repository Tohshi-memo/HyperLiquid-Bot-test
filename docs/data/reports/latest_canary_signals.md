# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T12:52:27.539906+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0244` n `13`; crypto_alt avg `0.0362` n `239`; crypto_major avg `0.0389` n `8`; equity avg `0.2266` n `166`; fx avg `0.0123` n `6`; index avg `0.0238` n `27`; metal avg `0.0984` n `20`; unknown avg `0.8552` n `1267`
- 1h: commodity avg `0.0125` n `13`; crypto_alt avg `-0.3302` n `239`; crypto_major avg `-0.1143` n `8`; equity avg `-0.1045` n `166`; fx avg `0.0128` n `6`; index avg `-0.0312` n `27`; metal avg `0.14` n `20`; unknown avg `249.5857` n `1252`
- 4h: commodity avg `0.194` n `13`; crypto_alt avg `-1.5766` n `239`; crypto_major avg `-0.6543` n `8`; equity avg `-1.4474` n `166`; fx avg `0.1266` n `6`; index avg `-0.2165` n `27`; metal avg `0.1715` n `20`; unknown avg `329.1831` n `1214`
- 24h: commodity avg `-0.4346` n `13`; crypto_alt avg `-1.33` n `239`; crypto_major avg `-0.9739` n `8`; equity avg `2.1215` n `166`; fx avg `0.0108` n `6`; index avg `0.3863` n `27`; metal avg `0.0508` n `20`; unknown avg `-0.1615` n `1142`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
