# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T09:52:33.607130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1606` n `12`; crypto_alt avg `-0.0117` n `234`; crypto_major avg `0.1206` n `8`; equity avg `0.2844` n `140`; fx avg `-0.0175` n `6`; index avg `0.0556` n `26`; metal avg `0.0811` n `20`; unknown avg `7.953` n `944`
- 1h: commodity avg `-0.0723` n `12`; crypto_alt avg `-0.5455` n `234`; crypto_major avg `-0.2796` n `8`; equity avg `0.3186` n `140`; fx avg `0.0149` n `6`; index avg `0.0569` n `26`; metal avg `-0.0394` n `20`; unknown avg `9.1166` n `942`
- 4h: commodity avg `-0.5791` n `12`; crypto_alt avg `0.1505` n `234`; crypto_major avg `0.3188` n `8`; equity avg `0.109` n `140`; fx avg `-0.0961` n `6`; index avg `0.0116` n `26`; metal avg `-0.0068` n `20`; unknown avg `8.0931` n `908`
- 24h: commodity avg `-0.6694` n `12`; crypto_alt avg `1.3979` n `234`; crypto_major avg `2.0584` n `8`; equity avg `0.9507` n `140`; fx avg `-0.2686` n `6`; index avg `0.2769` n `26`; metal avg `-0.0758` n `20`; unknown avg `1130.3779` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
