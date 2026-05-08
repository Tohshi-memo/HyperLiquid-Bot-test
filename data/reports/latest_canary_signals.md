# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T11:22:10.622295+00:00`
- Correlation status: `ready`
- Asset price records: `641`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1043` n `12`; crypto_alt avg `0.1445` n `228`; crypto_major avg `0.0623` n `8`; equity avg `-0.0375` n `65`; fx avg `-0.0135` n `5`; index avg `-0.0079` n `23`; metal avg `-0.1127` n `18`; unknown avg `-0.028` n `375`
- 1h: commodity avg `-0.0859` n `12`; crypto_alt avg `0.3432` n `228`; crypto_major avg `0.3337` n `8`; equity avg `-0.06` n `65`; fx avg `-0.0439` n `5`; index avg `-0.0075` n `23`; metal avg `0.0518` n `18`; unknown avg `-0.012` n `375`
- 4h: commodity avg `0.087` n `12`; crypto_alt avg `0.9205` n `228`; crypto_major avg `0.7713` n `8`; equity avg `0.5582` n `65`; fx avg `0.0048` n `5`; index avg `0.1527` n `23`; metal avg `0.3153` n `18`; unknown avg `0.5244` n `375`
- 24h: commodity avg `1.6216` n `12`; crypto_alt avg `1.0837` n `228`; crypto_major avg `-1.284` n `8`; equity avg `-0.5368` n `65`; fx avg `0.2309` n `5`; index avg `-0.397` n `23`; metal avg `-0.3144` n `18`; unknown avg `-0.3035` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1349`, n `633`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1347`, n `633`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `637`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `637`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0911`, n `637`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `633`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `637`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0795`, n `633`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `633`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `637`, weak_sample_signal
