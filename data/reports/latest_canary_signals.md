# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T05:22:26.813628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0972` n `13`; crypto_alt avg `-0.094` n `239`; crypto_major avg `0.0497` n `8`; equity avg `0.2729` n `168`; fx avg `0.0083` n `6`; index avg `0.0027` n `27`; metal avg `0.0792` n `20`; unknown avg `-0.3599` n `1261`
- 1h: commodity avg `0.132` n `13`; crypto_alt avg `0.1457` n `239`; crypto_major avg `0.3178` n `8`; equity avg `0.8094` n `168`; fx avg `0.0063` n `6`; index avg `0.0248` n `27`; metal avg `0.1329` n `20`; unknown avg `12.3822` n `1257`
- 4h: commodity avg `0.2856` n `13`; crypto_alt avg `1.2816` n `239`; crypto_major avg `2.1804` n `8`; equity avg `2.8838` n `168`; fx avg `0.026` n `6`; index avg `0.2249` n `27`; metal avg `0.9476` n `20`; unknown avg `66.4194` n `1251`
- 24h: commodity avg `0.373` n `13`; crypto_alt avg `1.819` n `239`; crypto_major avg `2.1007` n `8`; equity avg `3.1068` n `168`; fx avg `0.0382` n `6`; index avg `0.2565` n `27`; metal avg `0.76` n `20`; unknown avg `205.4782` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
