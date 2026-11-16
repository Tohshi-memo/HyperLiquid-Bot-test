# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T01:52:25.885153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0386` n `13`; crypto_alt avg `0.0387` n `239`; crypto_major avg `-0.0425` n `8`; equity avg `-0.0357` n `162`; fx avg `-0.019` n `6`; index avg `-0.0062` n `27`; metal avg `-0.008` n `20`; unknown avg `0.1527` n `1263`
- 1h: commodity avg `-0.0373` n `13`; crypto_alt avg `-0.7329` n `239`; crypto_major avg `-0.6684` n `8`; equity avg `-1.3917` n `162`; fx avg `-0.0017` n `6`; index avg `-0.171` n `27`; metal avg `-0.3889` n `20`; unknown avg `0.7745` n `1253`
- 4h: commodity avg `-0.2618` n `13`; crypto_alt avg `-0.676` n `239`; crypto_major avg `-0.8876` n `8`; equity avg `-0.5624` n `162`; fx avg `-0.0361` n `6`; index avg `-0.0445` n `27`; metal avg `-0.0798` n `20`; unknown avg `0.4464` n `1193`
- 24h: commodity avg `-0.3429` n `13`; crypto_alt avg `2.7425` n `239`; crypto_major avg `4.407` n `8`; equity avg `0.9584` n `162`; fx avg `-0.0166` n `6`; index avg `0.0753` n `27`; metal avg `0.286` n `20`; unknown avg `2.2649` n `1127`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
