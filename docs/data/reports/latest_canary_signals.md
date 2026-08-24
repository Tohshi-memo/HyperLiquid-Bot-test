# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T08:52:27.237372+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0635` n `12`; crypto_alt avg `0.2606` n `231`; crypto_major avg `0.2467` n `8`; equity avg `0.1671` n `122`; fx avg `-0.0165` n `6`; index avg `0.0211` n `25`; metal avg `0.0157` n `20`; unknown avg `0.5091` n `793`
- 1h: commodity avg `-0.0696` n `12`; crypto_alt avg `-0.3529` n `231`; crypto_major avg `-0.6629` n `8`; equity avg `0.2003` n `122`; fx avg `-0.0002` n `6`; index avg `0.039` n `25`; metal avg `-0.0211` n `20`; unknown avg `0.2905` n `793`
- 4h: commodity avg `0.0018` n `12`; crypto_alt avg `-0.2204` n `231`; crypto_major avg `-0.2231` n `8`; equity avg `-0.1279` n `122`; fx avg `0.0407` n `6`; index avg `-0.0206` n `25`; metal avg `-0.0044` n `20`; unknown avg `0.2186` n `777`
- 24h: commodity avg `-0.2549` n `12`; crypto_alt avg `1.9479` n `231`; crypto_major avg `0.0756` n `8`; equity avg `-1.2124` n `122`; fx avg `-0.1219` n `6`; index avg `-0.0989` n `25`; metal avg `0.1115` n `20`; unknown avg `5.2447` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
