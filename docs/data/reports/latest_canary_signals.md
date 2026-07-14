# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T01:37:24.856300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0366` n `12`; crypto_alt avg `-0.1567` n `230`; crypto_major avg `-0.2015` n `8`; equity avg `-0.2219` n `92`; fx avg `0.0153` n `6`; index avg `-0.0482` n `25`; metal avg `-0.0515` n `20`; unknown avg `-0.1646` n `766`
- 1h: commodity avg `-0.1286` n `12`; crypto_alt avg `0.098` n `230`; crypto_major avg `0.0497` n `8`; equity avg `-0.0205` n `92`; fx avg `-0.0522` n `6`; index avg `0.0449` n `25`; metal avg `-0.1053` n `20`; unknown avg `-0.2257` n `766`
- 4h: commodity avg `0.2563` n `12`; crypto_alt avg `1.1754` n `230`; crypto_major avg `1.0524` n `8`; equity avg `0.121` n `92`; fx avg `-0.0679` n `6`; index avg `0.0112` n `25`; metal avg `-0.1222` n `20`; unknown avg `0.4377` n `766`
- 24h: commodity avg `0.9164` n `12`; crypto_alt avg `-1.3336` n `230`; crypto_major avg `-1.9743` n `8`; equity avg `-1.9679` n `92`; fx avg `-0.1566` n `6`; index avg `-0.3779` n `25`; metal avg `-0.5031` n `20`; unknown avg `-0.3765` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
