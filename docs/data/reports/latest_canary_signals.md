# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T11:22:24.333027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `13`; crypto_alt avg `0.074` n `237`; crypto_major avg `0.0803` n `8`; equity avg `-0.0394` n `151`; fx avg `0.0116` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0004` n `20`; unknown avg `0.0387` n `1193`
- 1h: commodity avg `-0.0891` n `13`; crypto_alt avg `0.0061` n `237`; crypto_major avg `0.0208` n `8`; equity avg `-0.0138` n `151`; fx avg `0.0085` n `6`; index avg `-0.007` n `26`; metal avg `0.0011` n `20`; unknown avg `3.8114` n `1191`
- 4h: commodity avg `-0.0198` n `13`; crypto_alt avg `0.1817` n `237`; crypto_major avg `0.43` n `8`; equity avg `0.204` n `151`; fx avg `0.0145` n `6`; index avg `0.0231` n `26`; metal avg `0.0143` n `20`; unknown avg `4.8866` n `1079`
- 24h: commodity avg `0.0104` n `13`; crypto_alt avg `-2.2197` n `236`; crypto_major avg `-0.2397` n `8`; equity avg `-0.662` n `151`; fx avg `-0.0383` n `6`; index avg `-0.1003` n `26`; metal avg `-0.0481` n `20`; unknown avg `4.655` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2038`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1332`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1297`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.064`, n `666`, weak_sample_signal
