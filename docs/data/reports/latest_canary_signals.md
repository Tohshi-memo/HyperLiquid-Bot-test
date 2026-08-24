# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T08:37:28.313924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `-0.0662` n `231`; crypto_major avg `-0.0097` n `8`; equity avg `-0.036` n `122`; fx avg `0.0037` n `6`; index avg `0.0015` n `25`; metal avg `-0.0349` n `20`; unknown avg `0.0681` n `793`
- 1h: commodity avg `0.0448` n `12`; crypto_alt avg `-0.6674` n `231`; crypto_major avg `-0.907` n `8`; equity avg `-0.1513` n `122`; fx avg `-0.0056` n `6`; index avg `-0.0167` n `25`; metal avg `-0.1258` n `20`; unknown avg `-0.2563` n `793`
- 4h: commodity avg `0.0914` n `12`; crypto_alt avg `-0.867` n `231`; crypto_major avg `-0.9199` n `8`; equity avg `-0.3091` n `122`; fx avg `0.0439` n `6`; index avg `-0.0321` n `25`; metal avg `-0.0094` n `20`; unknown avg `-0.3732` n `777`
- 24h: commodity avg `-0.2121` n `12`; crypto_alt avg `1.7991` n `231`; crypto_major avg `-0.1345` n `8`; equity avg `-1.3706` n `122`; fx avg `-0.1038` n `6`; index avg `-0.1185` n `25`; metal avg `0.0912` n `20`; unknown avg `4.7609` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
