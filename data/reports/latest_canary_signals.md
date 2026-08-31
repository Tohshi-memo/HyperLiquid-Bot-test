# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T20:22:28.804389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `0.2409` n `232`; crypto_major avg `0.2258` n `8`; equity avg `0.0207` n `129`; fx avg `-0.0049` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0318` n `20`; unknown avg `-0.3463` n `781`
- 1h: commodity avg `0.087` n `12`; crypto_alt avg `0.18` n `232`; crypto_major avg `0.1794` n `8`; equity avg `0.3895` n `129`; fx avg `-0.0048` n `6`; index avg `0.0701` n `26`; metal avg `0.0623` n `20`; unknown avg `0.7973` n `779`
- 4h: commodity avg `0.0379` n `12`; crypto_alt avg `0.9102` n `232`; crypto_major avg `1.0885` n `8`; equity avg `0.5379` n `129`; fx avg `-0.0021` n `6`; index avg `0.0712` n `26`; metal avg `0.0578` n `20`; unknown avg `-0.3186` n `779`
- 24h: commodity avg `0.2301` n `12`; crypto_alt avg `-0.7338` n `231`; crypto_major avg `-0.5642` n `8`; equity avg `-0.0347` n `129`; fx avg `-0.0958` n `6`; index avg `-0.1633` n `26`; metal avg `-0.4348` n `20`; unknown avg `-0.0788` n `746`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
