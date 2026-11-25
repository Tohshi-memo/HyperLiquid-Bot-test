# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T05:52:29.319627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.074` n `13`; crypto_alt avg `0.1631` n `239`; crypto_major avg `0.2401` n `8`; equity avg `0.0544` n `168`; fx avg `-0.0043` n `6`; index avg `0.012` n `27`; metal avg `-0.0906` n `20`; unknown avg `2.6118` n `1265`
- 1h: commodity avg `-0.0253` n `13`; crypto_alt avg `0.3039` n `239`; crypto_major avg `0.204` n `8`; equity avg `-0.2756` n `168`; fx avg `-0.0029` n `6`; index avg `-0.0252` n `27`; metal avg `-0.2576` n `20`; unknown avg `4.4281` n `1261`
- 4h: commodity avg `-0.1471` n `13`; crypto_alt avg `0.9925` n `239`; crypto_major avg `0.2516` n `8`; equity avg `-0.9538` n `168`; fx avg `-0.0359` n `6`; index avg `-0.0399` n `27`; metal avg `-0.4321` n `20`; unknown avg `1.0087` n `1245`
- 24h: commodity avg `0.474` n `13`; crypto_alt avg `-3.5991` n `239`; crypto_major avg `-3.5641` n `8`; equity avg `-5.6577` n `167`; fx avg `0.1324` n `6`; index avg `-0.5578` n `27`; metal avg `-1.1519` n `20`; unknown avg `445.5436` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
