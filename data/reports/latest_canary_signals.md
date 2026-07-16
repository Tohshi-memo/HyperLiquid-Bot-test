# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T00:07:28.942237+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0` n `5`; crypto_alt avg `0.0971` n `230`; crypto_major avg `0.063` n `8`; equity avg `-0.0232` n `20`; fx avg `0.0` n `1`; index avg `0.0022` n `19`; metal avg `-0.0029` n `14`; unknown avg `0.0469` n `762`
- 1h: commodity avg `0.0` n `5`; crypto_alt avg `-0.0657` n `230`; crypto_major avg `-0.1425` n `8`; equity avg `-0.0687` n `20`; fx avg `0.0` n `1`; index avg `0.0016` n `19`; metal avg `-0.0072` n `14`; unknown avg `0.0598` n `762`
- 4h: commodity avg `0.0` n `5`; crypto_alt avg `0.1419` n `230`; crypto_major avg `0.1396` n `8`; equity avg `-0.0876` n `20`; fx avg `0.0` n `1`; index avg `0.003` n `19`; metal avg `-0.0042` n `14`; unknown avg `0.1925` n `762`
- 24h: commodity avg `0.0` n `5`; crypto_alt avg `0.1216` n `230`; crypto_major avg `0.2794` n `8`; equity avg `0.0415` n `19`; fx avg `0.0` n `1`; index avg `-0.0117` n `19`; metal avg `-0.0016` n `14`; unknown avg `0.1229` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
