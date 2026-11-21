# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T20:52:31.831101+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.0073` n `239`; crypto_major avg `-0.0545` n `8`; equity avg `-0.0755` n `166`; fx avg `-0.0032` n `6`; index avg `0.004` n `27`; metal avg `-0.0019` n `20`; unknown avg `162.6074` n `1262`
- 1h: commodity avg `0.0108` n `13`; crypto_alt avg `0.0861` n `239`; crypto_major avg `-0.0554` n `8`; equity avg `0.0747` n `166`; fx avg `0.0037` n `6`; index avg `0.0089` n `27`; metal avg `-0.0431` n `20`; unknown avg `205.2433` n `1236`
- 4h: commodity avg `0.0878` n `13`; crypto_alt avg `0.1309` n `239`; crypto_major avg `0.3991` n `8`; equity avg `0.1883` n `166`; fx avg `0.0257` n `6`; index avg `0.0623` n `27`; metal avg `0.0376` n `20`; unknown avg `0.7127` n `1190`
- 24h: commodity avg `-0.0027` n `13`; crypto_alt avg `1.7256` n `239`; crypto_major avg `3.3722` n `8`; equity avg `1.7695` n `166`; fx avg `-0.0633` n `6`; index avg `0.3041` n `27`; metal avg `0.2388` n `20`; unknown avg `0.4082` n `1074`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
