# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T02:37:29.456018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `13`; crypto_alt avg `-0.4144` n `239`; crypto_major avg `-0.4301` n `8`; equity avg `-0.14` n `166`; fx avg `0.0064` n `6`; index avg `-0.013` n `27`; metal avg `-0.0123` n `20`; unknown avg `6.4513` n `1262`
- 1h: commodity avg `0.0281` n `13`; crypto_alt avg `0.0054` n `239`; crypto_major avg `-0.2464` n `8`; equity avg `-0.1813` n `166`; fx avg `-0.0097` n `6`; index avg `-0.0148` n `27`; metal avg `-0.0088` n `20`; unknown avg `0.2595` n `1260`
- 4h: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.5982` n `239`; crypto_major avg `-0.8627` n `8`; equity avg `-0.1526` n `166`; fx avg `-0.0219` n `6`; index avg `0.0138` n `27`; metal avg `0.0006` n `20`; unknown avg `3.2897` n `1242`
- 24h: commodity avg `0.3306` n `13`; crypto_alt avg `-3.7895` n `239`; crypto_major avg `-5.0631` n `8`; equity avg `-4.9486` n `166`; fx avg `-0.0321` n `6`; index avg `-0.5604` n `27`; metal avg `-0.1383` n `20`; unknown avg `13.2226` n `1117`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
