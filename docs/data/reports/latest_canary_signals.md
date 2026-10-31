# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T06:07:34.652973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0416` n `13`; crypto_alt avg `0.2243` n `238`; crypto_major avg `0.1093` n `8`; equity avg `0.0159` n `156`; fx avg `0.003` n `6`; index avg `0.0048` n `27`; metal avg `0.0065` n `20`; unknown avg `-0.0476` n `1228`
- 1h: commodity avg `0.0175` n `13`; crypto_alt avg `-0.1034` n `238`; crypto_major avg `0.0338` n `8`; equity avg `0.021` n `156`; fx avg `0.0114` n `6`; index avg `0.0048` n `27`; metal avg `0.0056` n `20`; unknown avg `-0.2369` n `1228`
- 4h: commodity avg `0.147` n `13`; crypto_alt avg `-0.6508` n `238`; crypto_major avg `-0.3837` n `8`; equity avg `0.0198` n `156`; fx avg `-0.0012` n `6`; index avg `-0.0385` n `27`; metal avg `0.012` n `20`; unknown avg `-0.2799` n `1210`
- 24h: commodity avg `0.0287` n `13`; crypto_alt avg `0.9715` n `238`; crypto_major avg `-1.5372` n `8`; equity avg `-2.3419` n `156`; fx avg `-0.0783` n `6`; index avg `-0.1596` n `27`; metal avg `-0.5287` n `20`; unknown avg `4.3101` n `1002`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
