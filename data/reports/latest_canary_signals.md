# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T12:22:31.261827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0485` n `12`; crypto_alt avg `0.0698` n `228`; crypto_major avg `0.0671` n `8`; equity avg `0.118` n `79`; fx avg `0.019` n `6`; index avg `0.0116` n `23`; metal avg `-0.0051` n `20`; unknown avg `0.0001` n `722`
- 1h: commodity avg `-0.1552` n `12`; crypto_alt avg `0.5273` n `228`; crypto_major avg `0.4272` n `8`; equity avg `0.1652` n `79`; fx avg `0.0344` n `6`; index avg `0.0301` n `23`; metal avg `0.0101` n `20`; unknown avg `0.0769` n `722`
- 4h: commodity avg `-0.3532` n `12`; crypto_alt avg `1.0224` n `228`; crypto_major avg `0.572` n `8`; equity avg `0.4992` n `79`; fx avg `0.0576` n `6`; index avg `0.1322` n `23`; metal avg `0.2049` n `18`; unknown avg `0.5398` n `701`
- 24h: commodity avg `-0.5539` n `12`; crypto_alt avg `1.0983` n `228`; crypto_major avg `1.3112` n `8`; equity avg `0.2331` n `79`; fx avg `0.0849` n `6`; index avg `0.139` n `23`; metal avg `0.5541` n `18`; unknown avg `0.7173` n `637`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
