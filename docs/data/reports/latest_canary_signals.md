# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T13:07:27.727555+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `0.048` n `230`; crypto_major avg `0.0555` n `8`; equity avg `0.0764` n `92`; fx avg `0.0105` n `6`; index avg `0.0371` n `25`; metal avg `0.0195` n `20`; unknown avg `0.0085` n `766`
- 1h: commodity avg `-0.0551` n `12`; crypto_alt avg `-0.1801` n `230`; crypto_major avg `-0.3514` n `8`; equity avg `0.0485` n `92`; fx avg `0.0104` n `6`; index avg `0.061` n `25`; metal avg `0.0925` n `20`; unknown avg `0.0334` n `766`
- 4h: commodity avg `0.2408` n `12`; crypto_alt avg `-0.3042` n `230`; crypto_major avg `-0.6978` n `8`; equity avg `-0.0156` n `92`; fx avg `-0.015` n `6`; index avg `0.0245` n `25`; metal avg `-0.0307` n `20`; unknown avg `0.0285` n `766`
- 24h: commodity avg `-0.067` n `12`; crypto_alt avg `-1.4051` n `230`; crypto_major avg `-2.0514` n `8`; equity avg `-2.0967` n `92`; fx avg `-0.0451` n `6`; index avg `-0.403` n `25`; metal avg `-0.1821` n `20`; unknown avg `-0.2019` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1922`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
