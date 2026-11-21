# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T00:22:36.507980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `13`; crypto_alt avg `-0.172` n `239`; crypto_major avg `-0.1333` n `8`; equity avg `-0.0927` n `166`; fx avg `-0.0066` n `6`; index avg `-0.0018` n `27`; metal avg `-0.0056` n `20`; unknown avg `-0.0044` n `1260`
- 1h: commodity avg `-0.0151` n `13`; crypto_alt avg `-0.4903` n `239`; crypto_major avg `-0.2979` n `8`; equity avg `-0.4694` n `166`; fx avg `-0.0056` n `6`; index avg `-0.0378` n `27`; metal avg `-0.0223` n `20`; unknown avg `160.1385` n `1250`
- 4h: commodity avg `0.081` n `13`; crypto_alt avg `0.8562` n `239`; crypto_major avg `0.6665` n `8`; equity avg `0.8083` n `166`; fx avg `-0.0404` n `6`; index avg `0.0858` n `27`; metal avg `0.0781` n `20`; unknown avg `169.5363` n `1200`
- 24h: commodity avg `0.2693` n `13`; crypto_alt avg `-5.357` n `239`; crypto_major avg `-6.0954` n `8`; equity avg `-6.0697` n `166`; fx avg `-0.0523` n `6`; index avg `-0.705` n `27`; metal avg `-0.7655` n `20`; unknown avg `12.0757` n `1123`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
