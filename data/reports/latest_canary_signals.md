# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T06:52:24.291721+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0336` n `13`; crypto_alt avg `0.3244` n `239`; crypto_major avg `0.377` n `8`; equity avg `0.2329` n `162`; fx avg `0.0024` n `6`; index avg `0.0271` n `27`; metal avg `-0.0216` n `20`; unknown avg `0.1618` n `1260`
- 1h: commodity avg `0.0728` n `13`; crypto_alt avg `-0.3421` n `239`; crypto_major avg `-0.3814` n `8`; equity avg `-0.3183` n `162`; fx avg `-0.0015` n `6`; index avg `0.0051` n `27`; metal avg `-0.0967` n `20`; unknown avg `0.0183` n `1238`
- 4h: commodity avg `-0.0032` n `13`; crypto_alt avg `0.3903` n `239`; crypto_major avg `0.4757` n `8`; equity avg `-0.5592` n `162`; fx avg `-0.011` n `6`; index avg `-0.0636` n `27`; metal avg `0.0046` n `20`; unknown avg `-0.2805` n `1216`
- 24h: commodity avg `-1.2089` n `13`; crypto_alt avg `0.5916` n `239`; crypto_major avg `0.9786` n `8`; equity avg `-2.6535` n `162`; fx avg `-0.0136` n `6`; index avg `-0.2352` n `27`; metal avg `0.0083` n `20`; unknown avg `545.4774` n `1021`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
