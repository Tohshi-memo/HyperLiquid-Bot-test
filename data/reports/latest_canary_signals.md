# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T14:22:43.275268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-4.4842` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-2.2449` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0519` n `12`; crypto_alt avg `-0.0137` n `230`; crypto_major avg `0.0587` n `8`; equity avg `0.4164` n `102`; fx avg `-0.1228` n `6`; index avg `0.0651` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.047` n `779`
- 1h: commodity avg `0.1744` n `12`; crypto_alt avg `0.3439` n `230`; crypto_major avg `0.2695` n `8`; equity avg `2.5144` n `102`; fx avg `-0.386` n `6`; index avg `0.2231` n `25`; metal avg `0.1381` n `20`; unknown avg `0.1376` n `779`
- 4h: commodity avg `-0.0837` n `12`; crypto_alt avg `0.2218` n `230`; crypto_major avg `0.2` n `8`; equity avg `4.6842` n `102`; fx avg `-0.4178` n `6`; index avg `0.5144` n `25`; metal avg `0.1523` n `20`; unknown avg `0.0153` n `779`
- 24h: commodity avg `-0.0384` n `12`; crypto_alt avg `0.4812` n `230`; crypto_major avg `0.5386` n `8`; equity avg `3.3927` n `102`; fx avg `-0.4575` n `6`; index avg `0.291` n `25`; metal avg `0.7346` n `20`; unknown avg `-0.1604` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
