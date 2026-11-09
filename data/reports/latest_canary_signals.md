# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T08:52:27.241142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0668` n `13`; crypto_alt avg `0.6546` n `239`; crypto_major avg `0.4848` n `8`; equity avg `0.1851` n `158`; fx avg `0.0025` n `6`; index avg `0.0189` n `27`; metal avg `-0.0034` n `20`; unknown avg `0.3537` n `1253`
- 1h: commodity avg `0.0697` n `13`; crypto_alt avg `1.4299` n `239`; crypto_major avg `1.0683` n `8`; equity avg `1.0766` n `158`; fx avg `0.0732` n `6`; index avg `0.1238` n `27`; metal avg `0.1355` n `20`; unknown avg `0.7007` n `1151`
- 4h: commodity avg `-0.3686` n `13`; crypto_alt avg `-0.3294` n `239`; crypto_major avg `-0.541` n `8`; equity avg `-0.8878` n `158`; fx avg `0.0198` n `6`; index avg `-0.1294` n `27`; metal avg `-0.2486` n `20`; unknown avg `0.0369` n `1109`
- 24h: commodity avg `-0.1934` n `13`; crypto_alt avg `-2.1112` n `239`; crypto_major avg `-3.0838` n `8`; equity avg `-0.5982` n `158`; fx avg `-0.0706` n `6`; index avg `-0.0752` n `27`; metal avg `0.2515` n `20`; unknown avg `0.3878` n `948`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
