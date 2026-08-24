# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T17:07:24.098446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1332` n `12`; crypto_alt avg `-0.3841` n `231`; crypto_major avg `-0.2599` n `8`; equity avg `0.1013` n `122`; fx avg `-0.0129` n `6`; index avg `0.005` n `25`; metal avg `-0.0011` n `20`; unknown avg `0.0393` n `793`
- 1h: commodity avg `-0.0394` n `12`; crypto_alt avg `-0.5784` n `231`; crypto_major avg `-0.7468` n `8`; equity avg `0.0361` n `122`; fx avg `-0.0093` n `6`; index avg `0.0018` n `25`; metal avg `-0.0455` n `20`; unknown avg `0.5034` n `793`
- 4h: commodity avg `-0.4048` n `12`; crypto_alt avg `-0.6326` n `231`; crypto_major avg `-0.9609` n `8`; equity avg `-0.4464` n `122`; fx avg `-0.0223` n `6`; index avg `-0.0769` n `25`; metal avg `-0.1266` n `20`; unknown avg `-0.0035` n `793`
- 24h: commodity avg `-0.3046` n `12`; crypto_alt avg `-0.7856` n `231`; crypto_major avg `-0.1005` n `8`; equity avg `-2.2138` n `122`; fx avg `-0.1419` n `6`; index avg `-0.2909` n `25`; metal avg `0.1536` n `20`; unknown avg `3.4303` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
