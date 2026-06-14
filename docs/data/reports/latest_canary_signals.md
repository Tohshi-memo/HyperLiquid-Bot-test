# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T23:37:28.138520+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.1264` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `4.12` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.0706` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5405` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `0.1452` n `228`; crypto_major avg `0.3035` n `8`; equity avg `-0.0033` n `74`; fx avg `0.0041` n `6`; index avg `0.0074` n `23`; metal avg `0.0711` n `18`; unknown avg `-0.0815` n `637`
- 1h: commodity avg `-0.235` n `12`; crypto_alt avg `0.0918` n `228`; crypto_major avg `0.3164` n `8`; equity avg `-0.1452` n `74`; fx avg `0.0116` n `6`; index avg `-0.047` n `23`; metal avg `0.0849` n `18`; unknown avg `12.3968` n `637`
- 4h: commodity avg `-0.9758` n `12`; crypto_alt avg `2.7974` n `228`; crypto_major avg `3.1506` n `8`; equity avg `1.08` n `74`; fx avg `0.1235` n `6`; index avg `0.2233` n `23`; metal avg `1.6101` n `18`; unknown avg `3.5453` n `637`
- 24h: commodity avg `-0.8909` n `12`; crypto_alt avg `1.4835` n `228`; crypto_major avg `2.1039` n `8`; equity avg `1.2558` n `74`; fx avg `0.1021` n `6`; index avg `0.3618` n `23`; metal avg `1.4216` n `18`; unknown avg `1.3378` n `585`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
