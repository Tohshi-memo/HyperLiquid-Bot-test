# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T03:22:30.274981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2387` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `-0.0701` n `229`; crypto_major avg `-0.075` n `8`; equity avg `-0.0191` n `88`; fx avg `0.0` n `6`; index avg `0.0212` n `25`; metal avg `-0.0027` n `20`; unknown avg `0.0615` n `765`
- 1h: commodity avg `-0.0012` n `12`; crypto_alt avg `-0.1881` n `229`; crypto_major avg `-0.2149` n `8`; equity avg `0.0273` n `88`; fx avg `-0.0015` n `6`; index avg `0.0063` n `25`; metal avg `-0.0111` n `20`; unknown avg `-0.2499` n `765`
- 4h: commodity avg `0.0092` n `12`; crypto_alt avg `-1.0497` n `229`; crypto_major avg `-1.2403` n `8`; equity avg `0.0478` n `88`; fx avg `-0.0006` n `6`; index avg `-0.0016` n `25`; metal avg `-0.0269` n `20`; unknown avg `-0.419` n `763`
- 24h: commodity avg `0.0408` n `12`; crypto_alt avg `-0.976` n `229`; crypto_major avg `-0.8189` n `8`; equity avg `0.1605` n `88`; fx avg `0.0104` n `6`; index avg `0.0428` n `25`; metal avg `0.0834` n `20`; unknown avg `-0.981` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
