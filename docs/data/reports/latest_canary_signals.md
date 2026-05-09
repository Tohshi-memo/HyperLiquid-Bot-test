# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T11:52:15.419026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.1126` n `228`; crypto_major avg `0.0034` n `8`; equity avg `0.0018` n `65`; fx avg `-0.0134` n `5`; index avg `0.0009` n `23`; metal avg `0.0043` n `18`; unknown avg `0.1079` n `376`
- 1h: commodity avg `-0.0531` n `12`; crypto_alt avg `0.1214` n `228`; crypto_major avg `0.1312` n `8`; equity avg `0.0259` n `65`; fx avg `-0.0085` n `5`; index avg `-0.0149` n `23`; metal avg `0.018` n `18`; unknown avg `-0.3183` n `376`
- 4h: commodity avg `-0.1333` n `12`; crypto_alt avg `-0.1252` n `228`; crypto_major avg `-0.1062` n `8`; equity avg `0.1666` n `65`; fx avg `-0.0045` n `5`; index avg `-0.032` n `23`; metal avg `-0.0433` n `18`; unknown avg `-0.4174` n `376`
- 24h: commodity avg `-0.1508` n `12`; crypto_alt avg `3.0613` n `228`; crypto_major avg `1.9142` n `8`; equity avg `2.7349` n `65`; fx avg `-0.0348` n `5`; index avg `1.0767` n `23`; metal avg `-0.1147` n `18`; unknown avg `0.5046` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
