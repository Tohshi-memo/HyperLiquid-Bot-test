# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T22:22:34.619133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.177` n `12`; crypto_alt avg `0.0661` n `228`; crypto_major avg `0.0122` n `8`; equity avg `0.0041` n `74`; fx avg `0.005` n `6`; index avg `-0.0381` n `23`; metal avg `0.184` n `18`; unknown avg `0.3297` n `644`
- 1h: commodity avg `0.1204` n `12`; crypto_alt avg `0.6504` n `228`; crypto_major avg `0.3996` n `8`; equity avg `0.0509` n `74`; fx avg `-0.0223` n `6`; index avg `-0.011` n `23`; metal avg `0.061` n `18`; unknown avg `1.4093` n `644`
- 4h: commodity avg `0.3737` n `12`; crypto_alt avg `0.43` n `228`; crypto_major avg `0.5966` n `8`; equity avg `0.2053` n `74`; fx avg `-0.0287` n `6`; index avg `0.1481` n `23`; metal avg `0.271` n `18`; unknown avg `1.5998` n `644`
- 24h: commodity avg `-0.3599` n `12`; crypto_alt avg `2.4941` n `228`; crypto_major avg `1.2156` n `8`; equity avg `0.4543` n `74`; fx avg `0.0436` n `6`; index avg `0.4448` n `23`; metal avg `0.3367` n `18`; unknown avg `-0.0157` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
