# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T16:37:32.952043+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.765` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.5534` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0606` n `12`; crypto_alt avg `0.0557` n `229`; crypto_major avg `0.0657` n `8`; equity avg `0.0946` n `88`; fx avg `-0.0074` n `6`; index avg `-0.0242` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0207` n `766`
- 1h: commodity avg `-0.1608` n `12`; crypto_alt avg `1.4251` n `229`; crypto_major avg `1.4694` n `8`; equity avg `0.3152` n `88`; fx avg `0.0195` n `6`; index avg `0.0063` n `25`; metal avg `-0.084` n `20`; unknown avg `1.6229` n `765`
- 4h: commodity avg `0.0489` n `12`; crypto_alt avg `2.361` n `229`; crypto_major avg `1.7572` n `8`; equity avg `0.9141` n `88`; fx avg `0.0296` n `6`; index avg `0.1185` n `25`; metal avg `-0.0078` n `20`; unknown avg `1.1402` n `765`
- 24h: commodity avg `-0.107` n `12`; crypto_alt avg `1.3673` n `229`; crypto_major avg `0.9561` n `8`; equity avg `0.0406` n `88`; fx avg `0.1931` n `6`; index avg `0.078` n `25`; metal avg `-0.4019` n `20`; unknown avg `0.8262` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
