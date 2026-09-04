# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T08:37:25.411949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0028` n `232`; crypto_major avg `0.1523` n `8`; equity avg `0.0458` n `133`; fx avg `-0.0233` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0084` n `20`; unknown avg `0.0647` n `787`
- 1h: commodity avg `-0.0907` n `12`; crypto_alt avg `0.2397` n `232`; crypto_major avg `0.2211` n `8`; equity avg `0.2553` n `133`; fx avg `-0.0318` n `6`; index avg `0.0117` n `26`; metal avg `0.0893` n `20`; unknown avg `-0.0081` n `785`
- 4h: commodity avg `-0.124` n `12`; crypto_alt avg `-0.2932` n `232`; crypto_major avg `-0.3999` n `8`; equity avg `0.1655` n `133`; fx avg `-0.057` n `6`; index avg `0.0058` n `26`; metal avg `0.1088` n `20`; unknown avg `0.529` n `749`
- 24h: commodity avg `-0.1924` n `12`; crypto_alt avg `1.9304` n `232`; crypto_major avg `3.6563` n `8`; equity avg `1.8708` n `133`; fx avg `-0.0582` n `6`; index avg `0.3149` n `26`; metal avg `0.5089` n `20`; unknown avg `1.8075` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
