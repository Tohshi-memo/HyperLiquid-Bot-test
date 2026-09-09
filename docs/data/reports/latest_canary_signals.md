# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T18:52:34.317638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0586` n `12`; crypto_alt avg `-0.2335` n `233`; crypto_major avg `-0.1622` n `8`; equity avg `-0.0883` n `134`; fx avg `0.0082` n `6`; index avg `0.002` n `26`; metal avg `-0.0675` n `20`; unknown avg `-0.0652` n `797`
- 1h: commodity avg `0.0954` n `12`; crypto_alt avg `-0.1813` n `233`; crypto_major avg `-0.2529` n `8`; equity avg `-0.1442` n `134`; fx avg `-0.0115` n `6`; index avg `-0.006` n `26`; metal avg `-0.0912` n `20`; unknown avg `14.5055` n `795`
- 4h: commodity avg `-0.1203` n `12`; crypto_alt avg `-0.547` n `233`; crypto_major avg `-0.4937` n `8`; equity avg `-0.3626` n `134`; fx avg `0.0277` n `6`; index avg `-0.0856` n `26`; metal avg `-0.1596` n `20`; unknown avg `10.1999` n `789`
- 24h: commodity avg `0.0623` n `12`; crypto_alt avg `-0.0861` n `233`; crypto_major avg `0.1065` n `8`; equity avg `-0.3922` n `134`; fx avg `-0.0331` n `6`; index avg `-0.1693` n `26`; metal avg `0.554` n `20`; unknown avg `8.1571` n `699`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
