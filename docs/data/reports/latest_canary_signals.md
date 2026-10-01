# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T11:37:28.792099+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0193` n `13`; crypto_alt avg `0.1458` n `234`; crypto_major avg `0.0931` n `8`; equity avg `0.0365` n `142`; fx avg `-0.0088` n `6`; index avg `0.0155` n `26`; metal avg `0.0471` n `20`; unknown avg `0.0235` n `975`
- 1h: commodity avg `-0.0035` n `13`; crypto_alt avg `0.1533` n `234`; crypto_major avg `0.2331` n `8`; equity avg `-0.0274` n `142`; fx avg `-0.0025` n `6`; index avg `-0.0145` n `26`; metal avg `0.0118` n `20`; unknown avg `-0.2144` n `973`
- 4h: commodity avg `-0.1502` n `13`; crypto_alt avg `-0.3949` n `234`; crypto_major avg `0.3606` n `8`; equity avg `0.06` n `142`; fx avg `-0.0488` n `6`; index avg `0.0395` n `26`; metal avg `0.0538` n `20`; unknown avg `7.3189` n `957`
- 24h: commodity avg `-0.2016` n `13`; crypto_alt avg `-0.6477` n `234`; crypto_major avg `0.0613` n `8`; equity avg `0.5294` n `142`; fx avg `0.0327` n `6`; index avg `0.166` n `26`; metal avg `-0.1958` n `20`; unknown avg `773.9935` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1645`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
