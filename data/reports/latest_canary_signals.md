# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T13:37:25.252023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1766` n `12`; crypto_alt avg `-0.1557` n `228`; crypto_major avg `-0.1997` n `8`; equity avg `-0.0329` n `78`; fx avg `0.0001` n `6`; index avg `-0.0082` n `23`; metal avg `-0.0069` n `18`; unknown avg `0.0317` n `701`
- 1h: commodity avg `0.2305` n `12`; crypto_alt avg `-0.5457` n `228`; crypto_major avg `-0.5844` n `8`; equity avg `-0.2247` n `78`; fx avg `-0.0174` n `6`; index avg `-0.014` n `23`; metal avg `-0.0346` n `18`; unknown avg `0.1226` n `701`
- 4h: commodity avg `0.1349` n `12`; crypto_alt avg `-0.87` n `228`; crypto_major avg `-0.7247` n `8`; equity avg `-0.277` n `78`; fx avg `0.0071` n `6`; index avg `-0.0161` n `23`; metal avg `-0.0172` n `18`; unknown avg `-0.3084` n `573`
- 24h: commodity avg `0.6518` n `12`; crypto_alt avg `-3.7187` n `228`; crypto_major avg `-3.9846` n `8`; equity avg `0.9087` n `78`; fx avg `-0.085` n `6`; index avg `0.2817` n `23`; metal avg `-4.1248` n `18`; unknown avg `-0.3599` n `492`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
