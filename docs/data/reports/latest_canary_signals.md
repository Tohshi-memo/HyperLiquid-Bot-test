# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T13:22:34.574638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0071` n `13`; crypto_alt avg `0.0998` n `239`; crypto_major avg `0.3107` n `8`; equity avg `0.0319` n `162`; fx avg `-0.0084` n `6`; index avg `0.0037` n `27`; metal avg `0.0093` n `20`; unknown avg `-0.0351` n `1262`
- 1h: commodity avg `0.0091` n `13`; crypto_alt avg `0.1743` n `239`; crypto_major avg `0.4125` n `8`; equity avg `0.0825` n `162`; fx avg `-0.0161` n `6`; index avg `0.0055` n `27`; metal avg `-0.0044` n `20`; unknown avg `162.3688` n `1261`
- 4h: commodity avg `-0.0148` n `13`; crypto_alt avg `0.4719` n `239`; crypto_major avg `0.6182` n `8`; equity avg `0.0188` n `162`; fx avg `-0.0261` n `6`; index avg `0.0022` n `27`; metal avg `0.0211` n `20`; unknown avg `-0.0026` n `1253`
- 24h: commodity avg `0.0544` n `13`; crypto_alt avg `-2.9608` n `239`; crypto_major avg `-1.8336` n `8`; equity avg `-0.4984` n `162`; fx avg `-0.0129` n `6`; index avg `-0.0458` n `27`; metal avg `-0.296` n `20`; unknown avg `260.3677` n `1136`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
