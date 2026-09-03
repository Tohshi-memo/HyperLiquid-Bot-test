# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T13:52:26.057160+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0505` n `12`; crypto_alt avg `-0.0035` n `232`; crypto_major avg `0.1207` n `8`; equity avg `0.3688` n `133`; fx avg `-0.0192` n `6`; index avg `0.0751` n `26`; metal avg `-0.0594` n `20`; unknown avg `15.5306` n `792`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `-0.2748` n `232`; crypto_major avg `0.2584` n `8`; equity avg `-0.0476` n `133`; fx avg `0.0028` n `6`; index avg `0.0507` n `26`; metal avg `-0.1499` n `20`; unknown avg `15.8753` n `790`
- 4h: commodity avg `0.0248` n `12`; crypto_alt avg `0.3353` n `232`; crypto_major avg `1.267` n `8`; equity avg `0.3959` n `133`; fx avg `-0.0656` n `6`; index avg `0.1507` n `26`; metal avg `0.2017` n `20`; unknown avg `2.5913` n `790`
- 24h: commodity avg `0.5275` n `12`; crypto_alt avg `1.5635` n `232`; crypto_major avg `2.0439` n `8`; equity avg `1.2759` n `133`; fx avg `-0.313` n `6`; index avg `0.1838` n `26`; metal avg `0.3975` n `20`; unknown avg `-0.0074` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0429`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.04`, n `668`, weak_sample_signal
