# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T01:37:25.313416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `0.067` n `231`; crypto_major avg `0.0536` n `8`; equity avg `0.2488` n `122`; fx avg `0.0159` n `6`; index avg `0.0534` n `25`; metal avg `-0.004` n `20`; unknown avg `-0.0995` n `794`
- 1h: commodity avg `0.0427` n `12`; crypto_alt avg `0.5199` n `231`; crypto_major avg `0.7188` n `8`; equity avg `0.2749` n `122`; fx avg `0.0081` n `6`; index avg `0.0458` n `25`; metal avg `-0.0878` n `20`; unknown avg `0.4018` n `794`
- 4h: commodity avg `0.038` n `12`; crypto_alt avg `0.5269` n `231`; crypto_major avg `1.5972` n `8`; equity avg `0.1108` n `122`; fx avg `0.0298` n `6`; index avg `-0.0129` n `25`; metal avg `0.1294` n `20`; unknown avg `-0.0402` n `794`
- 24h: commodity avg `0.1194` n `12`; crypto_alt avg `1.0616` n `231`; crypto_major avg `1.9894` n `8`; equity avg `-2.0493` n `122`; fx avg `-0.0133` n `6`; index avg `-0.3112` n `25`; metal avg `0.3224` n `20`; unknown avg `0.4316` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0478`, n `668`, weak_sample_signal
