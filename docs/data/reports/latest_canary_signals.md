# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T11:52:23.465531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0924` n `12`; crypto_alt avg `-0.3014` n `228`; crypto_major avg `-0.3017` n `8`; equity avg `-0.186` n `72`; fx avg `0.024` n `6`; index avg `-0.0116` n `23`; metal avg `-0.0118` n `18`; unknown avg `-0.3594` n `420`
- 1h: commodity avg `-0.2767` n `12`; crypto_alt avg `-0.2508` n `228`; crypto_major avg `-0.4048` n `8`; equity avg `0.0189` n `72`; fx avg `0.0015` n `6`; index avg `0.0327` n `23`; metal avg `0.0888` n `18`; unknown avg `-0.0773` n `420`
- 4h: commodity avg `0.1392` n `12`; crypto_alt avg `-0.0562` n `228`; crypto_major avg `-0.5593` n `8`; equity avg `-0.2423` n `72`; fx avg `0.0278` n `6`; index avg `-0.0028` n `23`; metal avg `0.1587` n `18`; unknown avg `-0.4342` n `420`
- 24h: commodity avg `1.5213` n `12`; crypto_alt avg `-1.2075` n `228`; crypto_major avg `-3.5797` n `8`; equity avg `0.4414` n `72`; fx avg `0.0521` n `6`; index avg `0.8312` n `23`; metal avg `-1.384` n `18`; unknown avg `-0.3319` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
