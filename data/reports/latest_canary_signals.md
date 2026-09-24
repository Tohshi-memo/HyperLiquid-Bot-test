# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T20:07:32.700618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0842` n `12`; crypto_alt avg `-0.0848` n `234`; crypto_major avg `-0.1031` n `8`; equity avg `-0.1361` n `141`; fx avg `-0.0018` n `6`; index avg `-0.0274` n `26`; metal avg `-0.0175` n `20`; unknown avg `346.5588` n `934`
- 1h: commodity avg `-0.0388` n `12`; crypto_alt avg `0.2195` n `234`; crypto_major avg `-0.0131` n `8`; equity avg `-0.1313` n `141`; fx avg `-0.0098` n `6`; index avg `-0.0158` n `26`; metal avg `0.0027` n `20`; unknown avg `133.9379` n `905`
- 4h: commodity avg `-0.2295` n `12`; crypto_alt avg `0.8296` n `234`; crypto_major avg `0.7306` n `8`; equity avg `0.7801` n `141`; fx avg `-0.022` n `6`; index avg `0.1201` n `26`; metal avg `0.1994` n `20`; unknown avg `12.9595` n `905`
- 24h: commodity avg `0.9016` n `12`; crypto_alt avg `3.9641` n `234`; crypto_major avg `1.5013` n `8`; equity avg `-0.2295` n `141`; fx avg `0.0328` n `6`; index avg `-0.0956` n `26`; metal avg `-0.0668` n `20`; unknown avg `6.9956` n `843`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
