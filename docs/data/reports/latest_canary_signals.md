# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T02:22:32.111169+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1584` n `12`; crypto_alt avg `-0.2217` n `228`; crypto_major avg `-0.028` n `8`; equity avg `0.0705` n `74`; fx avg `0.0006` n `6`; index avg `0.0696` n `23`; metal avg `-0.0033` n `18`; unknown avg `0.2252` n `643`
- 1h: commodity avg `-0.0959` n `12`; crypto_alt avg `0.135` n `228`; crypto_major avg `0.1974` n `8`; equity avg `0.1847` n `74`; fx avg `0.0021` n `6`; index avg `0.1986` n `23`; metal avg `-0.018` n `18`; unknown avg `-0.439` n `643`
- 4h: commodity avg `-0.1953` n `12`; crypto_alt avg `0.6068` n `228`; crypto_major avg `-0.0144` n `8`; equity avg `0.2314` n `74`; fx avg `0.0375` n `6`; index avg `0.1832` n `23`; metal avg `0.0988` n `18`; unknown avg `-0.5377` n `643`
- 24h: commodity avg `-0.8028` n `12`; crypto_alt avg `0.2539` n `228`; crypto_major avg `0.0989` n `8`; equity avg `-0.5041` n `74`; fx avg `0.0167` n `6`; index avg `0.6918` n `23`; metal avg `0.4527` n `18`; unknown avg `40.6729` n `515`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0532`, n `668`, weak_sample_signal
