# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T04:07:19.664850+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0756` n `12`; crypto_alt avg `0.0012` n `228`; crypto_major avg `-0.0331` n `8`; equity avg `0.0217` n `67`; fx avg `0.0002` n `6`; index avg `0.0456` n `23`; metal avg `-0.0816` n `18`; unknown avg `-0.0699` n `407`
- 1h: commodity avg `0.0976` n `12`; crypto_alt avg `0.1821` n `228`; crypto_major avg `0.2552` n `8`; equity avg `0.1003` n `67`; fx avg `-0.0058` n `6`; index avg `0.049` n `23`; metal avg `0.0772` n `18`; unknown avg `0.2279` n `407`
- 4h: commodity avg `0.2074` n `12`; crypto_alt avg `-1.3201` n `228`; crypto_major avg `-1.0271` n `8`; equity avg `-0.1836` n `67`; fx avg `-0.0686` n `6`; index avg `-0.1759` n `23`; metal avg `-0.4263` n `18`; unknown avg `0.4581` n `407`
- 24h: commodity avg `0.549` n `12`; crypto_alt avg `-0.1794` n `228`; crypto_major avg `-0.8069` n `8`; equity avg `-0.4105` n `67`; fx avg `-0.014` n `6`; index avg `-0.0265` n `23`; metal avg `-0.1821` n `18`; unknown avg `0.2538` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1475`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
