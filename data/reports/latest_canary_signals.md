# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T21:22:41.491551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0025` n `13`; crypto_alt avg `0.1228` n `239`; crypto_major avg `0.2215` n `8`; equity avg `0.1894` n `168`; fx avg `-0.0051` n `6`; index avg `0.0189` n `27`; metal avg `0.0357` n `20`; unknown avg `3.0707` n `1259`
- 1h: commodity avg `0.0413` n `13`; crypto_alt avg `0.2761` n `239`; crypto_major avg `0.3821` n `8`; equity avg `0.3725` n `168`; fx avg `-0.012` n `6`; index avg `0.0569` n `27`; metal avg `0.0366` n `20`; unknown avg `1.2326` n `1233`
- 4h: commodity avg `0.0416` n `13`; crypto_alt avg `-0.1874` n `239`; crypto_major avg `0.256` n `8`; equity avg `0.4039` n `168`; fx avg `-0.0452` n `6`; index avg `0.0301` n `27`; metal avg `-0.0085` n `20`; unknown avg `381.672` n `1199`
- 24h: commodity avg `0.6211` n `13`; crypto_alt avg `-2.7392` n `239`; crypto_major avg `-2.5502` n `8`; equity avg `-3.8611` n `167`; fx avg `0.2271` n `6`; index avg `-0.2363` n `27`; metal avg `-1.0747` n `20`; unknown avg `409.0561` n `1111`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
