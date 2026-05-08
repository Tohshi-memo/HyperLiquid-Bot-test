# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T16:37:23.917411+00:00`
- Correlation status: `ready`
- Asset price records: `662`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3846` n `12`; crypto_alt avg `0.0553` n `228`; crypto_major avg `-0.0621` n `8`; equity avg `0.107` n `65`; fx avg `-0.009` n `5`; index avg `0.0792` n `23`; metal avg `0.1001` n `18`; unknown avg `0.0519` n `375`
- 1h: commodity avg `0.1162` n `12`; crypto_alt avg `0.7037` n `228`; crypto_major avg `0.3284` n `8`; equity avg `0.0791` n `65`; fx avg `0.0088` n `5`; index avg `0.0642` n `23`; metal avg `0.1667` n `18`; unknown avg `0.0328` n `375`
- 4h: commodity avg `0.4996` n `12`; crypto_alt avg `1.2023` n `228`; crypto_major avg `0.2633` n `8`; equity avg `1.0315` n `65`; fx avg `-0.0354` n `5`; index avg `0.3868` n `23`; metal avg `-0.4073` n `18`; unknown avg `0.1913` n `375`
- 24h: commodity avg `0.7071` n `12`; crypto_alt avg `2.8587` n `228`; crypto_major avg `0.3811` n `8`; equity avg `2.2068` n `65`; fx avg `0.1451` n `5`; index avg `0.8953` n `23`; metal avg `0.1285` n `18`; unknown avg `0.14` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.121`, n `654`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1168`, n `654`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `658`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1037`, n `654`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0994`, n `658`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0967`, n `654`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `658`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `658`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `658`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `658`, weak_sample_signal
