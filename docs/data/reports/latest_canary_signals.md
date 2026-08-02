# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T12:07:29.708919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `0.0096` n `230`; crypto_major avg `-0.0645` n `8`; equity avg `-0.0455` n `102`; fx avg `0.0074` n `6`; index avg `-0.0105` n `25`; metal avg `-0.0084` n `20`; unknown avg `-0.0186` n `782`
- 1h: commodity avg `0.1046` n `12`; crypto_alt avg `-0.0191` n `230`; crypto_major avg `-0.2199` n `8`; equity avg `-0.2455` n `102`; fx avg `0.0394` n `6`; index avg `-0.0548` n `25`; metal avg `-0.0162` n `20`; unknown avg `-0.0589` n `782`
- 4h: commodity avg `0.2725` n `12`; crypto_alt avg `-0.2899` n `230`; crypto_major avg `-0.5235` n `8`; equity avg `-0.2984` n `102`; fx avg `-0.0048` n `6`; index avg `-0.0826` n `25`; metal avg `-0.0271` n `20`; unknown avg `-0.0265` n `782`
- 24h: commodity avg `-0.9682` n `12`; crypto_alt avg `0.158` n `230`; crypto_major avg `0.0271` n `8`; equity avg `0.6373` n `102`; fx avg `-0.0881` n `6`; index avg `0.2094` n `25`; metal avg `0.2333` n `20`; unknown avg `0.2313` n `766`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
