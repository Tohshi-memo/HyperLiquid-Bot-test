# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T20:22:27.689363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `-0.0647` n `239`; crypto_major avg `-0.0418` n `8`; equity avg `0.0479` n `168`; fx avg `-0.001` n `6`; index avg `0.0028` n `27`; metal avg `0.0111` n `20`; unknown avg `0.843` n `1261`
- 1h: commodity avg `-0.0048` n `13`; crypto_alt avg `-0.1093` n `239`; crypto_major avg `0.0474` n `8`; equity avg `0.0904` n `168`; fx avg `0.0007` n `6`; index avg `0.0027` n `27`; metal avg `0.0461` n `20`; unknown avg `2.1283` n `1249`
- 4h: commodity avg `-0.0554` n `13`; crypto_alt avg `0.6542` n `239`; crypto_major avg `0.964` n `8`; equity avg `0.2972` n `168`; fx avg `-0.0164` n `6`; index avg `0.0231` n `27`; metal avg `-0.0228` n `20`; unknown avg `314.3839` n `1211`
- 24h: commodity avg `0.1331` n `13`; crypto_alt avg `1.652` n `239`; crypto_major avg `1.0365` n `8`; equity avg `1.4016` n `168`; fx avg `-0.041` n `6`; index avg `0.1039` n `27`; metal avg `0.1291` n `20`; unknown avg `12.8138` n `1031`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
