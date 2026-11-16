# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T12:07:36.352803+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `13`; crypto_alt avg `-0.3448` n `239`; crypto_major avg `-0.479` n `8`; equity avg `-0.414` n `162`; fx avg `-0.0079` n `6`; index avg `-0.053` n `27`; metal avg `-0.0642` n `20`; unknown avg `18.7035` n `1253`
- 1h: commodity avg `-0.0976` n `13`; crypto_alt avg `-0.572` n `239`; crypto_major avg `-0.8213` n `8`; equity avg `-0.6122` n `162`; fx avg `-0.0074` n `6`; index avg `-0.082` n `27`; metal avg `0.0177` n `20`; unknown avg `0.3621` n `1255`
- 4h: commodity avg `-0.2118` n `13`; crypto_alt avg `-0.149` n `239`; crypto_major avg `-0.3143` n `8`; equity avg `-0.8499` n `162`; fx avg `-0.0267` n `6`; index avg `-0.1015` n `27`; metal avg `0.0942` n `20`; unknown avg `17.2132` n `1251`
- 24h: commodity avg `-0.4485` n `13`; crypto_alt avg `-1.3491` n `239`; crypto_major avg `-1.2557` n `8`; equity avg `-1.3646` n `162`; fx avg `-0.0549` n `6`; index avg `-0.1182` n `27`; metal avg `0.0693` n `20`; unknown avg `24.5395` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1336`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1129`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1123`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1024`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.092`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0883`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0784`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0708`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0691`, n `669`, weak_sample_signal
