# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T01:22:37.865373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.016` n `13`; crypto_alt avg `-0.0665` n `239`; crypto_major avg `0.0134` n `8`; equity avg `-0.0007` n `166`; fx avg `0.0202` n `6`; index avg `0.0028` n `27`; metal avg `0.004` n `20`; unknown avg `0.6662` n `1261`
- 1h: commodity avg `0.0391` n `13`; crypto_alt avg `-0.1402` n `239`; crypto_major avg `-0.0522` n `8`; equity avg `0.0338` n `166`; fx avg `-0.0005` n `6`; index avg `-0.0004` n `27`; metal avg `0.0134` n `20`; unknown avg `7172.7072` n `1261`
- 4h: commodity avg `0.0086` n `13`; crypto_alt avg `-0.144` n `239`; crypto_major avg `-0.2137` n `8`; equity avg `0.0799` n `166`; fx avg `0.0156` n `6`; index avg `0.0343` n `27`; metal avg `-0.0329` n `20`; unknown avg `7480.4763` n `1236`
- 24h: commodity avg `0.0704` n `13`; crypto_alt avg `0.3553` n `239`; crypto_major avg `1.8022` n `8`; equity avg `0.6751` n `166`; fx avg `-0.0483` n `6`; index avg `0.1758` n `27`; metal avg `0.0976` n `20`; unknown avg `8369.4368` n `1080`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
