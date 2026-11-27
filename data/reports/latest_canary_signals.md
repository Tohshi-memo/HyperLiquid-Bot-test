# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T01:37:31.632121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0216` n `13`; crypto_alt avg `0.0529` n `239`; crypto_major avg `-0.0519` n `8`; equity avg `0.3468` n `168`; fx avg `0.0184` n `6`; index avg `0.0264` n `27`; metal avg `0.0362` n `20`; unknown avg `0.8653` n `1263`
- 1h: commodity avg `0.0146` n `13`; crypto_alt avg `0.2618` n `239`; crypto_major avg `0.2315` n `8`; equity avg `1.1314` n `168`; fx avg `0.0011` n `6`; index avg `0.1325` n `27`; metal avg `0.1432` n `20`; unknown avg `1.2287` n `1257`
- 4h: commodity avg `0.1178` n `13`; crypto_alt avg `-0.1029` n `239`; crypto_major avg `-0.4218` n `8`; equity avg `0.7246` n `168`; fx avg `-0.0113` n `6`; index avg `0.099` n `27`; metal avg `0.096` n `20`; unknown avg `3.4613` n `1205`
- 24h: commodity avg `0.1889` n `13`; crypto_alt avg `0.618` n `239`; crypto_major avg `0.4127` n `8`; equity avg `0.8448` n `168`; fx avg `0.0068` n `6`; index avg `0.0793` n `27`; metal avg `0.2738` n `20`; unknown avg `181.512` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
