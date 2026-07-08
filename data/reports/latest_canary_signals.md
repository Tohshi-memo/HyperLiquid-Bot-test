# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T18:51:18.665693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `0.2926` n `229`; crypto_major avg `0.2834` n `8`; equity avg `0.0805` n `91`; fx avg `0.0014` n `6`; index avg `0.0256` n `25`; metal avg `0.1185` n `20`; unknown avg `0.0762` n `764`
- 1h: commodity avg `0.0107` n `12`; crypto_alt avg `0.0597` n `229`; crypto_major avg `-0.1313` n `8`; equity avg `0.1936` n `91`; fx avg `-0.0219` n `6`; index avg `0.0263` n `25`; metal avg `0.185` n `20`; unknown avg `-0.1173` n `764`
- 4h: commodity avg `-0.4863` n `12`; crypto_alt avg `0.5248` n `229`; crypto_major avg `0.4459` n `8`; equity avg `0.7231` n `91`; fx avg `0.0033` n `6`; index avg `0.2309` n `25`; metal avg `0.3663` n `20`; unknown avg `-0.0997` n `764`
- 24h: commodity avg `0.5423` n `12`; crypto_alt avg `-2.4067` n `229`; crypto_major avg `-2.9309` n `8`; equity avg `0.6157` n `91`; fx avg `0.0118` n `6`; index avg `-0.0881` n `25`; metal avg `-0.8656` n `20`; unknown avg `-0.6251` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
