# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T11:22:30.733267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `0.1274` n `239`; crypto_major avg `-0.0049` n `8`; equity avg `-0.0937` n `163`; fx avg `0.004` n `6`; index avg `-0.0112` n `27`; metal avg `-0.0296` n `20`; unknown avg `0.2301` n `1264`
- 1h: commodity avg `0.1688` n `13`; crypto_alt avg `-0.1653` n `239`; crypto_major avg `-0.4604` n `8`; equity avg `-0.2365` n `163`; fx avg `0.0123` n `6`; index avg `-0.0287` n `27`; metal avg `-0.0486` n `20`; unknown avg `0.6011` n `1264`
- 4h: commodity avg `0.2615` n `13`; crypto_alt avg `-0.1535` n `239`; crypto_major avg `-0.6575` n `8`; equity avg `-0.0282` n `163`; fx avg `-0.0251` n `6`; index avg `0.0382` n `27`; metal avg `-0.2228` n `20`; unknown avg `48.3009` n `1186`
- 24h: commodity avg `-0.1065` n `13`; crypto_alt avg `0.4257` n `239`; crypto_major avg `0.5404` n `8`; equity avg `0.8908` n `163`; fx avg `-0.0887` n `6`; index avg `0.0781` n `27`; metal avg `-1.0879` n `20`; unknown avg `6.4633` n `1097`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
