# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T05:37:35.232174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `-0.0745` n `229`; crypto_major avg `0.0241` n `8`; equity avg `0.0181` n `88`; fx avg `0.0007` n `6`; index avg `0.0044` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.0233` n `765`
- 1h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.2711` n `229`; crypto_major avg `-0.3059` n `8`; equity avg `0.0014` n `88`; fx avg `-0.0002` n `6`; index avg `0.0461` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.7593` n `765`
- 4h: commodity avg `0.024` n `12`; crypto_alt avg `-0.3707` n `229`; crypto_major avg `-0.3394` n `8`; equity avg `0.1546` n `88`; fx avg `-0.0021` n `6`; index avg `0.0748` n `25`; metal avg `-0.0283` n `20`; unknown avg `-0.3763` n `765`
- 24h: commodity avg `0.0758` n `12`; crypto_alt avg `-0.8891` n `229`; crypto_major avg `-1.0934` n `8`; equity avg `0.1698` n `88`; fx avg `-0.0101` n `6`; index avg `0.0698` n `25`; metal avg `0.0781` n `20`; unknown avg `-0.8616` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
