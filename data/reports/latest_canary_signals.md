# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T12:07:28.484778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5018` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0403` n `12`; crypto_alt avg `0.0396` n `230`; crypto_major avg `0.0284` n `8`; equity avg `0.2178` n `102`; fx avg `0.0107` n `6`; index avg `0.0482` n `25`; metal avg `-0.009` n `20`; unknown avg `0.0126` n `779`
- 1h: commodity avg `-0.0608` n `12`; crypto_alt avg `0.3223` n `230`; crypto_major avg `0.2403` n `8`; equity avg `0.6272` n `102`; fx avg `0.0225` n `6`; index avg `0.1204` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0078` n `779`
- 4h: commodity avg `-0.29` n `12`; crypto_alt avg `0.3676` n `230`; crypto_major avg `0.8002` n `8`; equity avg `2.302` n `102`; fx avg `-0.0344` n `6`; index avg `0.3906` n `25`; metal avg `0.3224` n `20`; unknown avg `0.0787` n `771`
- 24h: commodity avg `0.2831` n `12`; crypto_alt avg `0.1378` n `230`; crypto_major avg `0.2469` n `8`; equity avg `-1.5146` n `102`; fx avg `-0.0402` n `6`; index avg `-0.2026` n `25`; metal avg `0.462` n `20`; unknown avg `-0.145` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
