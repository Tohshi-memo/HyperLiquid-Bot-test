# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T13:07:14.666679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `-0.1121` n `228`; crypto_major avg `-0.084` n `8`; equity avg `-0.0013` n `65`; fx avg `0.0` n `5`; index avg `0.0459` n `23`; metal avg `-0.0093` n `18`; unknown avg `0.196` n `376`
- 1h: commodity avg `0.1211` n `12`; crypto_alt avg `-0.353` n `228`; crypto_major avg `-0.2112` n `8`; equity avg `0.0433` n `65`; fx avg `0.0` n `5`; index avg `0.0381` n `23`; metal avg `-0.0282` n `18`; unknown avg `-0.0747` n `376`
- 4h: commodity avg `0.0037` n `12`; crypto_alt avg `-0.5872` n `228`; crypto_major avg `-0.337` n `8`; equity avg `0.073` n `65`; fx avg `-0.0036` n `5`; index avg `-0.0401` n `23`; metal avg `-0.0375` n `18`; unknown avg `-0.3835` n `376`
- 24h: commodity avg `-0.2123` n `12`; crypto_alt avg `3.0552` n `228`; crypto_major avg `2.1348` n `8`; equity avg `2.6565` n `65`; fx avg `-0.0011` n `5`; index avg `0.9968` n `23`; metal avg `-0.0499` n `18`; unknown avg `0.4831` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
