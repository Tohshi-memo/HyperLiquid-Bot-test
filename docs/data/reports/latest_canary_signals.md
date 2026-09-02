# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T17:22:32.835539+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0614` n `232`; crypto_major avg `-0.0467` n `8`; equity avg `0.0923` n `133`; fx avg `-0.0069` n `6`; index avg `0.0035` n `26`; metal avg `-0.0345` n `20`; unknown avg `-0.017` n `792`
- 1h: commodity avg `0.0024` n `12`; crypto_alt avg `-0.6648` n `232`; crypto_major avg `-0.794` n `8`; equity avg `0.0312` n `133`; fx avg `-0.0026` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0502` n `20`; unknown avg `0.0054` n `790`
- 4h: commodity avg `0.2639` n `12`; crypto_alt avg `0.0616` n `232`; crypto_major avg `0.1047` n `8`; equity avg `0.4435` n `133`; fx avg `-0.108` n `6`; index avg `0.1388` n `26`; metal avg `0.1072` n `20`; unknown avg `0.0083` n `789`
- 24h: commodity avg `0.4119` n `12`; crypto_alt avg `-0.9914` n `232`; crypto_major avg `-1.4851` n `8`; equity avg `0.0427` n `133`; fx avg `-0.3609` n `6`; index avg `0.0633` n `26`; metal avg `0.1482` n `20`; unknown avg `0.0396` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0474`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0446`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0417`, n `668`, weak_sample_signal
