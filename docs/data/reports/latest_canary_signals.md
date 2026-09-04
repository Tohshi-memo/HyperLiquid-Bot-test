# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T07:22:29.020521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `-0.015` n `232`; crypto_major avg `-0.1249` n `8`; equity avg `0.0896` n `133`; fx avg `-0.0027` n `6`; index avg `0.019` n `26`; metal avg `-0.0058` n `20`; unknown avg `0.037` n `793`
- 1h: commodity avg `0.1013` n `12`; crypto_alt avg `0.3464` n `232`; crypto_major avg `0.015` n `8`; equity avg `-0.0918` n `133`; fx avg `0.0062` n `6`; index avg `-0.0157` n `26`; metal avg `0.0329` n `20`; unknown avg `18.1704` n `789`
- 4h: commodity avg `-0.0354` n `12`; crypto_alt avg `-0.4099` n `232`; crypto_major avg `-0.2726` n `8`; equity avg `0.0507` n `133`; fx avg `-0.0214` n `6`; index avg `0.0368` n `26`; metal avg `-0.0121` n `20`; unknown avg `0.5418` n `755`
- 24h: commodity avg `0.0155` n `12`; crypto_alt avg `1.8255` n `232`; crypto_major avg `3.5753` n `8`; equity avg `1.6806` n `133`; fx avg `-0.0175` n `6`; index avg `0.3477` n `26`; metal avg `0.4734` n `20`; unknown avg `1.7366` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
