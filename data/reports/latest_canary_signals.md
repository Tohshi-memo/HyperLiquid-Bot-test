# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T06:37:29.024616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0679` n `13`; crypto_alt avg `0.0286` n `239`; crypto_major avg `-0.0943` n `8`; equity avg `-0.0823` n `158`; fx avg `-0.0067` n `6`; index avg `-0.0227` n `27`; metal avg `-0.0267` n `20`; unknown avg `0.0015` n `1259`
- 1h: commodity avg `-0.0299` n `13`; crypto_alt avg `0.0537` n `239`; crypto_major avg `-0.1519` n `8`; equity avg `-0.0629` n `158`; fx avg `-0.0054` n `6`; index avg `-0.0127` n `27`; metal avg `0.0638` n `20`; unknown avg `-0.1714` n `1235`
- 4h: commodity avg `-0.0868` n `13`; crypto_alt avg `-0.2676` n `239`; crypto_major avg `-0.3445` n `8`; equity avg `-1.0774` n `158`; fx avg `-0.0187` n `6`; index avg `-0.2263` n `27`; metal avg `-0.0842` n `20`; unknown avg `-0.1913` n `1211`
- 24h: commodity avg `-1.9393` n `13`; crypto_alt avg `1.1364` n `239`; crypto_major avg `2.1319` n `8`; equity avg `-2.5685` n `158`; fx avg `0.0681` n `6`; index avg `-0.1274` n `27`; metal avg `0.7995` n `20`; unknown avg `31.6352` n `1010`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2529`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
