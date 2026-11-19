# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T18:22:43.457316+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `2.5597` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `1.5029` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `0.4144` n `239`; crypto_major avg `0.5412` n `8`; equity avg `0.1303` n `165`; fx avg `0.011` n `6`; index avg `0.0129` n `27`; metal avg `0.0019` n `20`; unknown avg `0.2387` n `1260`
- 1h: commodity avg `0.0735` n `13`; crypto_alt avg `0.4835` n `239`; crypto_major avg `0.8439` n `8`; equity avg `-0.659` n `165`; fx avg `-0.0031` n `6`; index avg `-0.0564` n `27`; metal avg `-0.0251` n `20`; unknown avg `0.4783` n `1262`
- 4h: commodity avg `-0.1238` n `13`; crypto_alt avg `-1.532` n `239`; crypto_major avg `-0.8083` n `8`; equity avg `-3.368` n `165`; fx avg `-0.0595` n `6`; index avg `-0.4179` n `27`; metal avg `-0.3281` n `20`; unknown avg `10.0389` n `1255`
- 24h: commodity avg `0.345` n `13`; crypto_alt avg `-0.2941` n `239`; crypto_major avg `0.5641` n `8`; equity avg `-1.2348` n `165`; fx avg `0.0025` n `6`; index avg `-0.0567` n `27`; metal avg `-0.4773` n `20`; unknown avg `3.3231` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
