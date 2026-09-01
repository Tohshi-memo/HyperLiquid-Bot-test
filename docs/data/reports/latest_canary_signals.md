# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T11:52:25.596622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.038` n `12`; crypto_alt avg `0.1728` n `232`; crypto_major avg `0.1375` n `8`; equity avg `-0.0277` n `130`; fx avg `-0.0006` n `6`; index avg `-0.0057` n `26`; metal avg `0.0272` n `20`; unknown avg `-0.0779` n `792`
- 1h: commodity avg `-0.0941` n `12`; crypto_alt avg `0.4324` n `232`; crypto_major avg `0.2787` n `8`; equity avg `-0.032` n `130`; fx avg `0.0007` n `6`; index avg `0.0037` n `26`; metal avg `0.0485` n `20`; unknown avg `-0.0497` n `790`
- 4h: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.1241` n `232`; crypto_major avg `-0.0967` n `8`; equity avg `-1.1653` n `130`; fx avg `0.0194` n `6`; index avg `-0.2468` n `26`; metal avg `-0.417` n `20`; unknown avg `-0.2949` n `790`
- 24h: commodity avg `0.1033` n `12`; crypto_alt avg `1.2963` n `232`; crypto_major avg `0.5212` n `8`; equity avg `-0.5709` n `130`; fx avg `0.1153` n `6`; index avg `-0.2406` n `26`; metal avg `-0.7577` n `20`; unknown avg `-0.0769` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0472`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0369`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0288`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0286`, n `668`, weak_sample_signal
