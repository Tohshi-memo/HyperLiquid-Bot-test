# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T07:22:24.273819+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0765` n `12`; crypto_alt avg `-0.0218` n `231`; crypto_major avg `0.019` n `8`; equity avg `0.0437` n `127`; fx avg `-0.0216` n `6`; index avg `0.0032` n `26`; metal avg `-0.0075` n `20`; unknown avg `0.1228` n `792`
- 1h: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.2379` n `231`; crypto_major avg `-0.2431` n `8`; equity avg `-0.0145` n `127`; fx avg `-0.0111` n `6`; index avg `0.0064` n `26`; metal avg `0.2149` n `20`; unknown avg `0.0751` n `792`
- 4h: commodity avg `-0.0779` n `12`; crypto_alt avg `-0.1292` n `231`; crypto_major avg `-0.2771` n `8`; equity avg `-0.4685` n `127`; fx avg `-0.0762` n `6`; index avg `-0.0535` n `26`; metal avg `0.3077` n `20`; unknown avg `0.0073` n `760`
- 24h: commodity avg `0.4475` n `12`; crypto_alt avg `0.3034` n `231`; crypto_major avg `1.4183` n `8`; equity avg `-0.5242` n `127`; fx avg `-0.101` n `6`; index avg `0.0231` n `26`; metal avg `0.4705` n `20`; unknown avg `0.4633` n `759`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
