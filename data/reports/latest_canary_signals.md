# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T14:07:34.038980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0814` n `13`; crypto_alt avg `-0.2437` n `239`; crypto_major avg `-0.3301` n `8`; equity avg `0.007` n `162`; fx avg `-0.0236` n `6`; index avg `-0.0108` n `27`; metal avg `-0.0157` n `20`; unknown avg `5.3889` n `1256`
- 1h: commodity avg `0.0851` n `13`; crypto_alt avg `0.7856` n `239`; crypto_major avg `0.4191` n `8`; equity avg `0.2363` n `162`; fx avg `-0.0228` n `6`; index avg `-0.0064` n `27`; metal avg `-0.1299` n `20`; unknown avg `5.2365` n `1260`
- 4h: commodity avg `0.1481` n `13`; crypto_alt avg `1.2386` n `239`; crypto_major avg `0.8955` n `8`; equity avg `0.2747` n `162`; fx avg `-0.0045` n `6`; index avg `0.0099` n `27`; metal avg `-0.0946` n `20`; unknown avg `46.4485` n `1200`
- 24h: commodity avg `0.5506` n `13`; crypto_alt avg `1.5227` n `239`; crypto_major avg `-0.2411` n `8`; equity avg `1.0535` n `162`; fx avg `-0.0319` n `6`; index avg `0.1238` n `27`; metal avg `-0.1267` n `20`; unknown avg `2.6598` n `1073`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
