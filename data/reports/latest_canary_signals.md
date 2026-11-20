# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T22:37:32.823059+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.31` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0081` n `13`; crypto_alt avg `-0.0899` n `239`; crypto_major avg `-0.0307` n `8`; equity avg `0.3567` n `166`; fx avg `0.0034` n `6`; index avg `0.0214` n `27`; metal avg `0.0064` n `20`; unknown avg `0.221` n `1258`
- 1h: commodity avg `0.0039` n `13`; crypto_alt avg `0.7666` n `239`; crypto_major avg `0.7002` n `8`; equity avg `0.6166` n `166`; fx avg `-0.0089` n `6`; index avg `0.0567` n `27`; metal avg `0.0799` n `20`; unknown avg `160.9939` n `1246`
- 4h: commodity avg `0.5076` n `13`; crypto_alt avg `0.2772` n `239`; crypto_major avg `-0.0632` n `8`; equity avg `-0.4077` n `166`; fx avg `-0.0375` n `6`; index avg `-0.1299` n `27`; metal avg `0.0534` n `20`; unknown avg `0.6291` n `1206`
- 24h: commodity avg `0.2637` n `13`; crypto_alt avg `-5.1173` n `239`; crypto_major avg `-5.6857` n `8`; equity avg `-6.3708` n `166`; fx avg `0.0142` n `6`; index avg `-0.7144` n `27`; metal avg `-0.8477` n `20`; unknown avg `32.0582` n `1129`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
