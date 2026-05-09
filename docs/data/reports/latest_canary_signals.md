# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T20:52:17.893927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0045` n `12`; crypto_alt avg `0.1058` n `228`; crypto_major avg `0.0055` n `8`; equity avg `-0.0272` n `65`; fx avg `0.0` n `5`; index avg `0.0614` n `23`; metal avg `0.0038` n `18`; unknown avg `-0.0267` n `376`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `-0.0933` n `228`; crypto_major avg `-0.1736` n `8`; equity avg `0.232` n `65`; fx avg `0.0289` n `5`; index avg `0.0733` n `23`; metal avg `0.0361` n `18`; unknown avg `0.0174` n `376`
- 4h: commodity avg `0.0175` n `12`; crypto_alt avg `0.5676` n `228`; crypto_major avg `0.2634` n `8`; equity avg `0.3134` n `65`; fx avg `0.0172` n `5`; index avg `0.1095` n `23`; metal avg `0.1465` n `18`; unknown avg `0.0947` n `376`
- 24h: commodity avg `0.3599` n `12`; crypto_alt avg `0.6808` n `228`; crypto_major avg `0.4907` n `8`; equity avg `0.7726` n `65`; fx avg `-0.0251` n `5`; index avg `0.4364` n `23`; metal avg `0.0689` n `18`; unknown avg `0.13` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
