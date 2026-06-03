# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T12:07:23.841303+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.073` n `12`; crypto_alt avg `0.1486` n `228`; crypto_major avg `0.1299` n `8`; equity avg `-0.062` n `72`; fx avg `-0.043` n `6`; index avg `0.002` n `23`; metal avg `-0.0648` n `18`; unknown avg `-0.0624` n `420`
- 1h: commodity avg `-0.2613` n `12`; crypto_alt avg `-0.5162` n `228`; crypto_major avg `-0.4024` n `8`; equity avg `-0.0676` n `72`; fx avg `-0.0223` n `6`; index avg `0.0321` n `23`; metal avg `-0.0684` n `18`; unknown avg `-0.2537` n `420`
- 4h: commodity avg `0.0149` n `12`; crypto_alt avg `0.3244` n `228`; crypto_major avg `-0.2531` n `8`; equity avg `-0.0946` n `72`; fx avg `-0.0125` n `6`; index avg `0.037` n `23`; metal avg `0.1805` n `18`; unknown avg `-0.3723` n `420`
- 24h: commodity avg `1.5932` n `12`; crypto_alt avg `-0.8148` n `228`; crypto_major avg `-3.3328` n `8`; equity avg `0.4605` n `72`; fx avg `0.016` n `6`; index avg `0.8803` n `23`; metal avg `-1.3324` n `18`; unknown avg `-0.2168` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0443`, n `668`, weak_sample_signal
