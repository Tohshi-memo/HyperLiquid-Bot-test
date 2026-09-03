# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T18:52:31.531308+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0461` n `12`; crypto_alt avg `0.2078` n `232`; crypto_major avg `0.2951` n `8`; equity avg `0.0167` n `133`; fx avg `-0.002` n `6`; index avg `0.0012` n `26`; metal avg `-0.0217` n `20`; unknown avg `0.3797` n `792`
- 1h: commodity avg `0.0145` n `12`; crypto_alt avg `0.2889` n `232`; crypto_major avg `0.0658` n `8`; equity avg `0.07` n `133`; fx avg `0.0078` n `6`; index avg `0.0181` n `26`; metal avg `-0.0714` n `20`; unknown avg `-0.3748` n `790`
- 4h: commodity avg `-0.2045` n `12`; crypto_alt avg `1.6151` n `232`; crypto_major avg `1.4106` n `8`; equity avg `1.2633` n `133`; fx avg `0.0376` n `6`; index avg `0.2457` n `26`; metal avg `0.1883` n `20`; unknown avg `2.2683` n `790`
- 24h: commodity avg `-0.0643` n `12`; crypto_alt avg `4.6888` n `232`; crypto_major avg `5.4392` n `8`; equity avg `1.6897` n `133`; fx avg `-0.2591` n `6`; index avg `0.2236` n `26`; metal avg `0.8484` n `20`; unknown avg `1.1176` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
