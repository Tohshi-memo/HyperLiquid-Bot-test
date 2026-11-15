# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T13:37:36.356931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0665` n `13`; crypto_alt avg `-0.1529` n `239`; crypto_major avg `-0.2783` n `8`; equity avg `-0.0056` n `162`; fx avg `0.0028` n `6`; index avg `-0.001` n `27`; metal avg `-0.0138` n `20`; unknown avg `0.0217` n `1264`
- 1h: commodity avg `-0.074` n `13`; crypto_alt avg `-0.0092` n `239`; crypto_major avg `0.1018` n `8`; equity avg `0.054` n `162`; fx avg `-0.0222` n `6`; index avg `0.0047` n `27`; metal avg `-0.0093` n `20`; unknown avg `158.3966` n `1261`
- 4h: commodity avg `-0.0894` n `13`; crypto_alt avg `0.6108` n `239`; crypto_major avg `0.7417` n `8`; equity avg `0.0469` n `162`; fx avg `-0.0335` n `6`; index avg `-0.0007` n `27`; metal avg `0.016` n `20`; unknown avg `-0.083` n `1253`
- 24h: commodity avg `-0.0169` n `13`; crypto_alt avg `-2.9976` n `239`; crypto_major avg `-2.0705` n `8`; equity avg `-0.4421` n `162`; fx avg `-0.0099` n `6`; index avg `-0.0449` n `27`; metal avg `-0.3146` n `20`; unknown avg `260.3371` n `1136`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
