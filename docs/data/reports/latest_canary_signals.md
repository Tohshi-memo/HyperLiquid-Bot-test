# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T02:22:26.631793+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `0.0904` n `230`; crypto_major avg `-0.065` n `8`; equity avg `0.0928` n `121`; fx avg `0.0036` n `6`; index avg `0.0276` n `25`; metal avg `0.0248` n `20`; unknown avg `-0.2601` n `793`
- 1h: commodity avg `0.0317` n `12`; crypto_alt avg `0.7157` n `230`; crypto_major avg `0.5979` n `8`; equity avg `0.578` n `121`; fx avg `-0.0277` n `6`; index avg `0.0817` n `25`; metal avg `0.0454` n `20`; unknown avg `-0.103` n `793`
- 4h: commodity avg `0.1122` n `12`; crypto_alt avg `1.1261` n `230`; crypto_major avg `1.6223` n `8`; equity avg `0.9246` n `121`; fx avg `-0.1033` n `6`; index avg `0.1536` n `25`; metal avg `0.217` n `20`; unknown avg `-0.3497` n `793`
- 24h: commodity avg `0.3944` n `12`; crypto_alt avg `5.3423` n `230`; crypto_major avg `6.6185` n `8`; equity avg `-0.2693` n `121`; fx avg `-0.0206` n `6`; index avg `-0.0701` n `25`; metal avg `0.4887` n `20`; unknown avg `2.646` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
