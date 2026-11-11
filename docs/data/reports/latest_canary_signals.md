# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T08:37:26.652331+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `-0.2722` n `239`; crypto_major avg `-0.3664` n `8`; equity avg `0.067` n `161`; fx avg `-0.0069` n `6`; index avg `0.0152` n `27`; metal avg `0.049` n `20`; unknown avg `0.0676` n `1261`
- 1h: commodity avg `0.0178` n `13`; crypto_alt avg `0.1369` n `239`; crypto_major avg `-0.0283` n `8`; equity avg `0.5928` n `161`; fx avg `-0.0339` n `6`; index avg `0.0467` n `27`; metal avg `0.0135` n `20`; unknown avg `0.2381` n `1237`
- 4h: commodity avg `-0.0058` n `13`; crypto_alt avg `-0.9296` n `239`; crypto_major avg `-0.3016` n `8`; equity avg `0.6613` n `161`; fx avg `-0.0773` n `6`; index avg `0.0297` n `27`; metal avg `0.2156` n `20`; unknown avg `0.0418` n `1201`
- 24h: commodity avg `0.574` n `13`; crypto_alt avg `-1.2629` n `239`; crypto_major avg `-2.2019` n `8`; equity avg `1.9257` n `161`; fx avg `-0.2162` n `6`; index avg `0.205` n `27`; metal avg `0.0067` n `20`; unknown avg `1.3754` n `1158`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1332`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
