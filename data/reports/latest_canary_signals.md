# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T20:10:15.992452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0595` n `12`; crypto_alt avg `-0.0435` n `234`; crypto_major avg `-0.0031` n `8`; equity avg `-0.124` n `140`; fx avg `-0.01` n `6`; index avg `-0.0348` n `26`; metal avg `-0.0677` n `20`; unknown avg `48.8609` n `934`
- 1h: commodity avg `-0.0911` n `12`; crypto_alt avg `-0.0203` n `234`; crypto_major avg `-0.287` n `8`; equity avg `0.0562` n `140`; fx avg `-0.0235` n `6`; index avg `0.0178` n `26`; metal avg `0.0262` n `20`; unknown avg `11.2555` n `934`
- 4h: commodity avg `-0.1522` n `12`; crypto_alt avg `0.8444` n `234`; crypto_major avg `0.2905` n `8`; equity avg `0.4592` n `140`; fx avg `-0.0179` n `6`; index avg `0.0862` n `26`; metal avg `0.3849` n `20`; unknown avg `6.1799` n `894`
- 24h: commodity avg `0.1221` n `12`; crypto_alt avg `1.9891` n `234`; crypto_major avg `0.6799` n `8`; equity avg `0.8701` n `140`; fx avg `-0.2927` n `6`; index avg `0.1298` n `26`; metal avg `0.3045` n `20`; unknown avg `1.1611` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
