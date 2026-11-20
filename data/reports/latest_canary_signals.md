# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T05:52:28.775559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0637` n `13`; crypto_alt avg `0.6036` n `239`; crypto_major avg `0.7305` n `8`; equity avg `0.3429` n `165`; fx avg `0.0094` n `6`; index avg `0.0454` n `27`; metal avg `0.2871` n `20`; unknown avg `12.2663` n `1262`
- 1h: commodity avg `-0.1162` n `13`; crypto_alt avg `0.839` n `239`; crypto_major avg `0.9745` n `8`; equity avg `-0.0736` n `165`; fx avg `-0.005` n `6`; index avg `-0.007` n `27`; metal avg `0.1509` n `20`; unknown avg `45.6298` n `1254`
- 4h: commodity avg `-0.0999` n `13`; crypto_alt avg `-0.377` n `239`; crypto_major avg `0.0945` n `8`; equity avg `-0.3772` n `165`; fx avg `0.0332` n `6`; index avg `-0.0372` n `27`; metal avg `-0.0732` n `20`; unknown avg `0.5457` n `1244`
- 24h: commodity avg `-0.1822` n `13`; crypto_alt avg `-2.6101` n `239`; crypto_major avg `-2.0207` n `8`; equity avg `-5.8948` n `165`; fx avg `0.0174` n `6`; index avg `-0.5095` n `27`; metal avg `-1.734` n `20`; unknown avg `240.1045` n `1165`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
