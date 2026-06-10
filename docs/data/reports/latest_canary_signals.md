# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T18:07:33.684080+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3161` n `12`; crypto_alt avg `0.1096` n `228`; crypto_major avg `0.0743` n `8`; equity avg `0.2307` n `74`; fx avg `0.0219` n `6`; index avg `0.1548` n `23`; metal avg `0.243` n `18`; unknown avg `0.007` n `550`
- 1h: commodity avg `-0.2296` n `12`; crypto_alt avg `-0.7146` n `228`; crypto_major avg `-0.7123` n `8`; equity avg `0.1514` n `74`; fx avg `-0.0075` n `6`; index avg `0.086` n `23`; metal avg `-0.0618` n `18`; unknown avg `-0.0905` n `548`
- 4h: commodity avg `0.0599` n `12`; crypto_alt avg `-1.4389` n `228`; crypto_major avg `-1.4932` n `8`; equity avg `-1.1038` n `74`; fx avg `-0.0277` n `6`; index avg `-0.7758` n `23`; metal avg `-0.7834` n `18`; unknown avg `0.0145` n `547`
- 24h: commodity avg `1.2814` n `12`; crypto_alt avg `-0.7153` n `228`; crypto_major avg `-1.6107` n `8`; equity avg `0.0878` n `74`; fx avg `-0.0494` n `6`; index avg `0.1331` n `23`; metal avg `-1.263` n `18`; unknown avg `-0.0938` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0584`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
