# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T01:08:03.703003+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1019` n `12`; crypto_alt avg `0.1451` n `234`; crypto_major avg `0.0522` n `8`; equity avg `0.1384` n `142`; fx avg `-0.0107` n `6`; index avg `0.0438` n `26`; metal avg `0.1184` n `20`; unknown avg `0.2428` n `973`
- 1h: commodity avg `-0.0666` n `12`; crypto_alt avg `0.2055` n `234`; crypto_major avg `-0.0154` n `8`; equity avg `0.034` n `142`; fx avg `0.049` n `6`; index avg `0.0347` n `26`; metal avg `0.0185` n `20`; unknown avg `2.0836` n `949`
- 4h: commodity avg `-0.0877` n `12`; crypto_alt avg `0.7771` n `234`; crypto_major avg `0.034` n `8`; equity avg `0.318` n `142`; fx avg `0.103` n `6`; index avg `0.1222` n `26`; metal avg `-0.0481` n `20`; unknown avg `0.6191` n `943`
- 24h: commodity avg `0.1123` n `12`; crypto_alt avg `0.7216` n `234`; crypto_major avg `0.806` n `8`; equity avg `-0.1491` n `142`; fx avg `0.1412` n `6`; index avg `0.0553` n `26`; metal avg `-0.2128` n `20`; unknown avg `775.2218` n `797`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
