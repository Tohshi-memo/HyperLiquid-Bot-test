# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T07:52:29.014585+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0192` n `13`; crypto_alt avg `0.004` n `239`; crypto_major avg `-0.0196` n `8`; equity avg `0.1093` n `166`; fx avg `0.0119` n `6`; index avg `0.0083` n `27`; metal avg `0.0289` n `20`; unknown avg `-0.1132` n `1264`
- 1h: commodity avg `0.1472` n `13`; crypto_alt avg `-0.4311` n `239`; crypto_major avg `-0.3853` n `8`; equity avg `-0.3185` n `166`; fx avg `-0.0138` n `6`; index avg `-0.0478` n `27`; metal avg `-0.0109` n `20`; unknown avg `11.8325` n `1252`
- 4h: commodity avg `0.161` n `13`; crypto_alt avg `0.9245` n `239`; crypto_major avg `0.3068` n `8`; equity avg `-0.0902` n `166`; fx avg `0.0398` n `6`; index avg `-0.0145` n `27`; metal avg `-0.0885` n `20`; unknown avg `277.236` n `1204`
- 24h: commodity avg `-0.8268` n `13`; crypto_alt avg `0.3205` n `239`; crypto_major avg `-0.1832` n `8`; equity avg `4.0999` n `166`; fx avg `-0.2379` n `6`; index avg `0.6445` n `27`; metal avg `-0.2414` n `20`; unknown avg `689.2192` n `1032`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
