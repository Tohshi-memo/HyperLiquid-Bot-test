# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T22:22:16.225672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0818` n `228`; crypto_major avg `0.003` n `8`; equity avg `0.0453` n `65`; fx avg `0.0` n `5`; index avg `0.011` n `23`; metal avg `-0.0187` n `18`; unknown avg `-0.1826` n `376`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `0.1027` n `228`; crypto_major avg `0.0537` n `8`; equity avg `0.078` n `65`; fx avg `0.0` n `5`; index avg `0.0611` n `23`; metal avg `0.0531` n `18`; unknown avg `-0.0802` n `376`
- 4h: commodity avg `-0.0077` n `12`; crypto_alt avg `0.1434` n `228`; crypto_major avg `-0.0021` n `8`; equity avg `0.4069` n `65`; fx avg `-0.0083` n `5`; index avg `0.1004` n `23`; metal avg `0.1627` n `18`; unknown avg `-0.2029` n `376`
- 24h: commodity avg `0.5298` n `12`; crypto_alt avg `0.1222` n `228`; crypto_major avg `0.2207` n `8`; equity avg `0.6831` n `65`; fx avg `-0.0291` n `5`; index avg `0.3274` n `23`; metal avg `0.1155` n `18`; unknown avg `0.1217` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
