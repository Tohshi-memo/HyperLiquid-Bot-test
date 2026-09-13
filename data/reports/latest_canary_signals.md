# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T05:37:29.411809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0086` n `12`; crypto_alt avg `-0.0856` n `233`; crypto_major avg `0.0223` n `8`; equity avg `-0.0569` n `136`; fx avg `-0.0016` n `6`; index avg `-0.0092` n `26`; metal avg `0.0007` n `20`; unknown avg `-0.0791` n `838`
- 1h: commodity avg `0.0394` n `12`; crypto_alt avg `0.0776` n `233`; crypto_major avg `0.1672` n `8`; equity avg `-0.0965` n `136`; fx avg `-0.0088` n `6`; index avg `-0.0211` n `26`; metal avg `0.009` n `20`; unknown avg `0.0135` n `836`
- 4h: commodity avg `0.0709` n `12`; crypto_alt avg `0.1642` n `233`; crypto_major avg `0.0034` n `8`; equity avg `-0.2548` n `136`; fx avg `0.0018` n `6`; index avg `-0.0528` n `26`; metal avg `0.0027` n `20`; unknown avg `-0.1662` n `806`
- 24h: commodity avg `0.1354` n `12`; crypto_alt avg `1.0049` n `233`; crypto_major avg `0.1709` n `8`; equity avg `-0.5964` n `136`; fx avg `-0.0101` n `6`; index avg `-0.0832` n `26`; metal avg `0.0347` n `20`; unknown avg `3.7696` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0501`, n `668`, weak_sample_signal
