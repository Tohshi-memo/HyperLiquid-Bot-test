# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T04:07:18.964641+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `12`; crypto_alt avg `-0.0658` n `228`; crypto_major avg `-0.0239` n `8`; equity avg `0.0331` n `67`; fx avg `-0.0009` n `6`; index avg `0.1406` n `23`; metal avg `0.0674` n `18`; unknown avg `-0.1159` n `397`
- 1h: commodity avg `-0.2896` n `12`; crypto_alt avg `0.0103` n `228`; crypto_major avg `-0.0419` n `8`; equity avg `0.1854` n `67`; fx avg `0.0112` n `6`; index avg `0.0915` n `23`; metal avg `0.1191` n `18`; unknown avg `-0.2703` n `397`
- 4h: commodity avg `-0.5147` n `12`; crypto_alt avg `-0.0232` n `228`; crypto_major avg `-0.4806` n `8`; equity avg `0.4122` n `67`; fx avg `-0.0889` n `6`; index avg `0.3479` n `23`; metal avg `-0.3084` n `18`; unknown avg `-0.3067` n `396`
- 24h: commodity avg `-0.0044` n `12`; crypto_alt avg `-1.0037` n `228`; crypto_major avg `-0.2287` n `8`; equity avg `0.6163` n `67`; fx avg `-0.0501` n `6`; index avg `-0.0748` n `23`; metal avg `0.4114` n `18`; unknown avg `-0.1523` n `386`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
