# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T11:22:21.567690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0775` n `12`; crypto_alt avg `0.131` n `228`; crypto_major avg `0.1889` n `8`; equity avg `0.2009` n `72`; fx avg `0.0138` n `6`; index avg `0.0488` n `23`; metal avg `-0.0467` n `18`; unknown avg `0.8409` n `420`
- 1h: commodity avg `-0.2866` n `12`; crypto_alt avg `0.7937` n `228`; crypto_major avg `0.3582` n `8`; equity avg `0.3336` n `72`; fx avg `0.0234` n `6`; index avg `0.0348` n `23`; metal avg `-0.0358` n `18`; unknown avg `0.8664` n `420`
- 4h: commodity avg `0.4149` n `12`; crypto_alt avg `0.8653` n `228`; crypto_major avg `0.3538` n `8`; equity avg `-0.0019` n `72`; fx avg `-0.0054` n `6`; index avg `0.0159` n `23`; metal avg `-0.0045` n `18`; unknown avg `0.7738` n `420`
- 24h: commodity avg `1.714` n `12`; crypto_alt avg `-0.275` n `228`; crypto_major avg `-2.7395` n `8`; equity avg `0.7826` n `72`; fx avg `0.052` n `6`; index avg `0.9601` n `23`; metal avg `-1.3111` n `18`; unknown avg `0.6746` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0588`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0484`, n `668`, weak_sample_signal
