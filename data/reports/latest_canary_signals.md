# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T21:07:29.943045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.0574` n `234`; crypto_major avg `0.0625` n `8`; equity avg `0.0071` n `141`; fx avg `-0.04` n `6`; index avg `-0.0003` n `26`; metal avg `-0.002` n `20`; unknown avg `24.2387` n `960`
- 1h: commodity avg `0.0306` n `12`; crypto_alt avg `-0.4211` n `234`; crypto_major avg `-0.1655` n `8`; equity avg `-0.0253` n `141`; fx avg `-0.0548` n `6`; index avg `-0.0036` n `26`; metal avg `-0.0068` n `20`; unknown avg `24.5318` n `960`
- 4h: commodity avg `0.0452` n `12`; crypto_alt avg `0.402` n `234`; crypto_major avg `0.3178` n `8`; equity avg `0.1237` n `141`; fx avg `-0.0602` n `6`; index avg `0.0233` n `26`; metal avg `-0.0013` n `20`; unknown avg `3.0685` n `928`
- 24h: commodity avg `-0.1294` n `12`; crypto_alt avg `1.2885` n `234`; crypto_major avg `0.6866` n `8`; equity avg `0.425` n `141`; fx avg `-0.0589` n `6`; index avg `0.0459` n `26`; metal avg `-0.0126` n `20`; unknown avg `8.2526` n `871`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
