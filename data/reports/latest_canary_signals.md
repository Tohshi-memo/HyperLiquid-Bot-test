# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T07:52:32.483333+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `13`; crypto_alt avg `0.047` n `239`; crypto_major avg `0.0395` n `8`; equity avg `0.0912` n `158`; fx avg `0.0077` n `6`; index avg `0.0168` n `27`; metal avg `0.0529` n `20`; unknown avg `0.1653` n `1265`
- 1h: commodity avg `0.2852` n `13`; crypto_alt avg `-0.4261` n `239`; crypto_major avg `-0.2101` n `8`; equity avg `-0.0067` n `158`; fx avg `-0.0168` n `6`; index avg `0.0363` n `27`; metal avg `-0.0387` n `20`; unknown avg `0.1302` n `1257`
- 4h: commodity avg `0.3831` n `13`; crypto_alt avg `-0.796` n `239`; crypto_major avg `-0.3052` n `8`; equity avg `-0.2793` n `158`; fx avg `-0.0485` n `6`; index avg `-0.0509` n `27`; metal avg `-0.1521` n `20`; unknown avg `-0.1089` n `1209`
- 24h: commodity avg `-1.6981` n `13`; crypto_alt avg `0.4482` n `239`; crypto_major avg `1.8813` n `8`; equity avg `-2.2759` n `158`; fx avg `0.0204` n `6`; index avg `-0.0854` n `27`; metal avg `0.7595` n `20`; unknown avg `30.7892` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.25`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
