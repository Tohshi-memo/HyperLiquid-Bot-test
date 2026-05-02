# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T18:00:35.859056+00:00`
- Correlation status: `ready`
- Asset price records: `95`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `7`; crypto_alt avg `-0.0752` n `223`; crypto_major avg `-0.0306` n `7`; equity avg `0.0933` n `42`; fx avg `-0.0021` n `4`; index avg `0.0016` n `9`; metal avg `-0.016` n `7`; unknown avg `0.0129` n `313`
- 1h: commodity avg `-0.1352` n `7`; crypto_alt avg `-0.3612` n `223`; crypto_major avg `-0.1973` n `7`; equity avg `0.1239` n `42`; fx avg `-0.0043` n `4`; index avg `0.0076` n `9`; metal avg `-0.0338` n `7`; unknown avg `-0.0314` n `313`
- 4h: commodity avg `-0.1706` n `7`; crypto_alt avg `0.8331` n `223`; crypto_major avg `0.012` n `7`; equity avg `0.093` n `42`; fx avg `0.0933` n `4`; index avg `0.0072` n `9`; metal avg `-0.0285` n `7`; unknown avg `-0.0039` n `313`
- 24h: commodity avg `0.2145` n `7`; crypto_alt avg `1.3795` n `223`; crypto_major avg `0.2895` n `7`; equity avg `0.7702` n `42`; fx avg `-0.0468` n `4`; index avg `0.1375` n `9`; metal avg `-0.4952` n `7`; unknown avg `0.8564` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5252`, n `91`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5229`, n `87`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5069`, n `91`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.4943`, n `87`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4597`, n `87`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4545`, n `87`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4478`, n `87`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4454`, n `91`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4171`, n `87`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4128`, n `87`, moderate_sample_signal
