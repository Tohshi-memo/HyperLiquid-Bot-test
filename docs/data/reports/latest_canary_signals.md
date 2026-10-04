# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T13:22:25.161551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `13`; crypto_alt avg `0.0921` n `235`; crypto_major avg `0.0574` n `8`; equity avg `0.0033` n `144`; fx avg `0.0017` n `6`; index avg `0.0003` n `26`; metal avg `-0.003` n `20`; unknown avg `0.3729` n `1078`
- 1h: commodity avg `0.0387` n `13`; crypto_alt avg `0.2133` n `235`; crypto_major avg `-0.059` n `8`; equity avg `0.0083` n `144`; fx avg `-0.0026` n `6`; index avg `-0.0076` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.2497` n `1076`
- 4h: commodity avg `0.0478` n `13`; crypto_alt avg `-0.2523` n `235`; crypto_major avg `-0.0143` n `8`; equity avg `0.0283` n `144`; fx avg `0.0249` n `6`; index avg `0.0006` n `26`; metal avg `-0.016` n `20`; unknown avg `-0.0737` n `1070`
- 24h: commodity avg `0.1912` n `13`; crypto_alt avg `1.8464` n `235`; crypto_major avg `1.2592` n `8`; equity avg `0.2718` n `144`; fx avg `0.0067` n `6`; index avg `0.0311` n `26`; metal avg `-0.0028` n `20`; unknown avg `-0.226` n `901`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2062`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1511`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
