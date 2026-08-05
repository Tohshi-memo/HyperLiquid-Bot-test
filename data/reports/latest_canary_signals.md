# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T03:22:31.321779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `-0.3513` n `230`; crypto_major avg `-0.4345` n `8`; equity avg `0.0343` n `108`; fx avg `-0.0015` n `6`; index avg `-0.0117` n `25`; metal avg `-0.0248` n `20`; unknown avg `1.7797` n `781`
- 1h: commodity avg `-0.0794` n `12`; crypto_alt avg `-0.1764` n `230`; crypto_major avg `-0.3141` n `8`; equity avg `0.2043` n `108`; fx avg `-0.0202` n `6`; index avg `-0.0011` n `25`; metal avg `0.2485` n `20`; unknown avg `0.465` n `781`
- 4h: commodity avg `-0.0652` n `12`; crypto_alt avg `-0.0945` n `230`; crypto_major avg `-0.1834` n `8`; equity avg `0.6197` n `108`; fx avg `-0.1181` n `6`; index avg `0.0335` n `25`; metal avg `0.4205` n `20`; unknown avg `0.1016` n `781`
- 24h: commodity avg `-1.5023` n `12`; crypto_alt avg `0.1778` n `230`; crypto_major avg `0.5578` n `8`; equity avg `4.1749` n `108`; fx avg `-0.0201` n `6`; index avg `0.8532` n `25`; metal avg `1.0688` n `20`; unknown avg `0.3888` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
