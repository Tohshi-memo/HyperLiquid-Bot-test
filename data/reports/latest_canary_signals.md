# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T14:37:30.949503+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-4.6309` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.8947` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1304` n `12`; crypto_alt avg `-0.0686` n `230`; crypto_major avg `0.0582` n `8`; equity avg `0.082` n `102`; fx avg `0.038` n `6`; index avg `-0.0016` n `25`; metal avg `0.0967` n `20`; unknown avg `0.0111` n `779`
- 1h: commodity avg `0.2356` n `12`; crypto_alt avg `0.498` n `230`; crypto_major avg `0.5941` n `8`; equity avg `2.4888` n `102`; fx avg `-0.0671` n `6`; index avg `0.2385` n `25`; metal avg `0.0873` n `20`; unknown avg `0.1199` n `779`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `0.378` n `230`; crypto_major avg `0.4483` n `8`; equity avg `5.0792` n `102`; fx avg `-0.2981` n `6`; index avg `0.5601` n `25`; metal avg `0.1636` n `20`; unknown avg `0.0493` n `779`
- 24h: commodity avg `-0.0499` n `12`; crypto_alt avg `0.8349` n `230`; crypto_major avg `1.0582` n `8`; equity avg `4.5865` n `102`; fx avg `-0.3838` n `6`; index avg `0.4302` n `25`; metal avg `0.8076` n `20`; unknown avg `-0.0853` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
