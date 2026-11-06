# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T22:52:25.611453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `13`; crypto_alt avg `-0.0527` n `239`; crypto_major avg `-0.0967` n `8`; equity avg `-0.052` n `158`; fx avg `0.0067` n `6`; index avg `0.0095` n `27`; metal avg `-0.0063` n `20`; unknown avg `3.1255` n `1261`
- 1h: commodity avg `0.0111` n `13`; crypto_alt avg `-0.2156` n `239`; crypto_major avg `0.1048` n `8`; equity avg `-0.072` n `158`; fx avg `0.0051` n `6`; index avg `0.003` n `27`; metal avg `0.0111` n `20`; unknown avg `-0.2213` n `1247`
- 4h: commodity avg `0.122` n `13`; crypto_alt avg `-0.3321` n `239`; crypto_major avg `-0.0763` n `8`; equity avg `0.3208` n `158`; fx avg `0.0155` n `6`; index avg `-0.0319` n `27`; metal avg `-0.0577` n `20`; unknown avg `-0.2051` n `1181`
- 24h: commodity avg `0.0547` n `13`; crypto_alt avg `1.7604` n `239`; crypto_major avg `0.3248` n `8`; equity avg `3.09` n `158`; fx avg `-0.0671` n `6`; index avg `0.4138` n `27`; metal avg `0.0514` n `20`; unknown avg `0.2146` n `1034`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
