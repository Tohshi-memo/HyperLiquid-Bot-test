# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T03:22:28.990153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0106` n `12`; crypto_alt avg `0.2107` n `229`; crypto_major avg `0.2103` n `8`; equity avg `0.0043` n `88`; fx avg `0.0094` n `6`; index avg `0.0036` n `25`; metal avg `-0.0003` n `20`; unknown avg `-0.2047` n `765`
- 1h: commodity avg `0.0052` n `12`; crypto_alt avg `0.3866` n `229`; crypto_major avg `0.34` n `8`; equity avg `0.0991` n `88`; fx avg `-0.0003` n `6`; index avg `0.0047` n `25`; metal avg `0.0034` n `20`; unknown avg `-0.447` n `765`
- 4h: commodity avg `0.0123` n `12`; crypto_alt avg `-0.1575` n `229`; crypto_major avg `-0.0763` n `8`; equity avg `0.1355` n `88`; fx avg `-0.0207` n `6`; index avg `-0.0352` n `25`; metal avg `-0.0343` n `20`; unknown avg `-0.1143` n `763`
- 24h: commodity avg `-0.0182` n `12`; crypto_alt avg `2.2542` n `229`; crypto_major avg `2.681` n `8`; equity avg `0.881` n `88`; fx avg `-0.1948` n `6`; index avg `0.1631` n `25`; metal avg `-0.1401` n `20`; unknown avg `4.7155` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
