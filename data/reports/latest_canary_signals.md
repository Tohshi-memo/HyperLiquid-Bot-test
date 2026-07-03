# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T04:07:29.765084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0267` n `12`; crypto_alt avg `-0.1178` n `229`; crypto_major avg `-0.0714` n `8`; equity avg `0.1938` n `88`; fx avg `-0.0145` n `6`; index avg `0.0585` n `25`; metal avg `-0.0078` n `20`; unknown avg `0.0013` n `765`
- 1h: commodity avg `0.0605` n `12`; crypto_alt avg `-0.1469` n `229`; crypto_major avg `-0.0012` n `8`; equity avg `0.2464` n `88`; fx avg `0.0078` n `6`; index avg `0.0739` n `25`; metal avg `-0.0477` n `20`; unknown avg `-0.267` n `765`
- 4h: commodity avg `0.214` n `12`; crypto_alt avg `0.3988` n `229`; crypto_major avg `0.1377` n `8`; equity avg `1.132` n `88`; fx avg `-0.0104` n `6`; index avg `0.2478` n `25`; metal avg `0.5709` n `20`; unknown avg `0.332` n `761`
- 24h: commodity avg `0.4006` n `12`; crypto_alt avg `1.443` n `228`; crypto_major avg `2.2342` n `8`; equity avg `-0.9018` n `88`; fx avg `-0.0192` n `6`; index avg `-0.1276` n `25`; metal avg `1.0686` n `20`; unknown avg `6.2064` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0538`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
