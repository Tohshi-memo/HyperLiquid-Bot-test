# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T13:52:16.644519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0309` n `12`; crypto_alt avg `0.0513` n `228`; crypto_major avg `-0.019` n `8`; equity avg `0.071` n `65`; fx avg `0.0` n `5`; index avg `0.0041` n `23`; metal avg `-0.0512` n `18`; unknown avg `0.0887` n `376`
- 1h: commodity avg `-0.1191` n `12`; crypto_alt avg `0.3572` n `228`; crypto_major avg `0.2937` n `8`; equity avg `0.0679` n `65`; fx avg `-0.0004` n `5`; index avg `0.0253` n `23`; metal avg `0.1268` n `18`; unknown avg `-0.2854` n `376`
- 4h: commodity avg `-0.0963` n `12`; crypto_alt avg `0.1129` n `228`; crypto_major avg `-0.0439` n `8`; equity avg `0.1162` n `65`; fx avg `-0.0102` n `5`; index avg `0.0064` n `23`; metal avg `0.2526` n `18`; unknown avg `-0.3844` n `376`
- 24h: commodity avg `-0.0864` n `12`; crypto_alt avg `0.5398` n `228`; crypto_major avg `0.147` n `8`; equity avg `0.9378` n `65`; fx avg `-0.0089` n `5`; index avg `0.2583` n `23`; metal avg `0.6699` n `18`; unknown avg `0.1833` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
