# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T22:22:28.395018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `12`; crypto_alt avg `-0.2587` n `232`; crypto_major avg `-0.2531` n `8`; equity avg `-0.0861` n `131`; fx avg `0.0049` n `6`; index avg `-0.0102` n `26`; metal avg `-0.0079` n `20`; unknown avg `-0.0488` n `793`
- 1h: commodity avg `0.099` n `12`; crypto_alt avg `-0.222` n `232`; crypto_major avg `-0.1324` n `8`; equity avg `-0.1953` n `131`; fx avg `0.0068` n `6`; index avg `-0.019` n `26`; metal avg `-0.0308` n `20`; unknown avg `-0.0674` n `791`
- 4h: commodity avg `0.3025` n `12`; crypto_alt avg `0.1941` n `232`; crypto_major avg `-0.032` n `8`; equity avg `-0.1732` n `131`; fx avg `0.0139` n `6`; index avg `-0.0061` n `26`; metal avg `-0.1044` n `20`; unknown avg `2.1816` n `773`
- 24h: commodity avg `0.9266` n `12`; crypto_alt avg `-0.6615` n `232`; crypto_major avg `-2.2323` n `8`; equity avg `-2.2018` n `130`; fx avg `0.0557` n `6`; index avg `-0.3432` n `26`; metal avg `-0.8954` n `20`; unknown avg `-0.3881` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0442`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0392`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0308`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0307`, n `668`, weak_sample_signal
