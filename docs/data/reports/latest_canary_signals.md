# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T00:07:44.184983+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0042` n `13`; crypto_alt avg `-0.029` n `239`; crypto_major avg `-0.1413` n `8`; equity avg `-0.1953` n `168`; fx avg `0.0342` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0006` n `20`; unknown avg `39.8764` n `1249`
- 1h: commodity avg `0.0159` n `13`; crypto_alt avg `-0.2182` n `239`; crypto_major avg `-0.5105` n `8`; equity avg `-0.8951` n `168`; fx avg `0.058` n `6`; index avg `-0.0908` n `27`; metal avg `-0.0624` n `20`; unknown avg `288.7453` n `1239`
- 4h: commodity avg `0.0582` n `13`; crypto_alt avg `0.115` n `239`; crypto_major avg `0.202` n `8`; equity avg `-0.0538` n `168`; fx avg `0.037` n `6`; index avg `-0.0148` n `27`; metal avg `0.0154` n `20`; unknown avg `1.0574` n `1163`
- 24h: commodity avg `0.5509` n `13`; crypto_alt avg `-2.8871` n `239`; crypto_major avg `-2.3831` n `8`; equity avg `-4.4324` n `167`; fx avg `0.2945` n `6`; index avg `-0.3206` n `27`; metal avg `-1.1014` n `20`; unknown avg `657.5675` n `1057`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
