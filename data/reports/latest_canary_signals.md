# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T18:22:24.628360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.1232` n `230`; crypto_major avg `0.127` n `8`; equity avg `0.0655` n `92`; fx avg `0.0` n `6`; index avg `0.0042` n `25`; metal avg `0.0012` n `20`; unknown avg `-0.0251` n `765`
- 1h: commodity avg `0.0326` n `12`; crypto_alt avg `0.3294` n `230`; crypto_major avg `0.2017` n `8`; equity avg `0.1159` n `92`; fx avg `-0.0007` n `6`; index avg `0.0118` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.0159` n `765`
- 4h: commodity avg `0.0523` n `12`; crypto_alt avg `0.3198` n `230`; crypto_major avg `0.3056` n `8`; equity avg `0.2421` n `92`; fx avg `-0.0048` n `6`; index avg `0.0273` n `25`; metal avg `-0.0205` n `20`; unknown avg `0.2786` n `765`
- 24h: commodity avg `0.0858` n `12`; crypto_alt avg `1.1371` n `229`; crypto_major avg `0.7744` n `8`; equity avg `0.2229` n `92`; fx avg `0.0008` n `6`; index avg `0.0439` n `25`; metal avg `0.075` n `20`; unknown avg `2.4322` n `727`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
