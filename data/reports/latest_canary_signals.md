# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T13:37:30.516120+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.54` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0703` n `13`; crypto_alt avg `0.1541` n `239`; crypto_major avg `0.181` n `8`; equity avg `0.2667` n `163`; fx avg `0.01` n `6`; index avg `0.0261` n `27`; metal avg `0.0517` n `20`; unknown avg `0.2241` n `1266`
- 1h: commodity avg `0.0782` n `13`; crypto_alt avg `0.2429` n `239`; crypto_major avg `0.1267` n `8`; equity avg `0.0632` n `163`; fx avg `0.0233` n `6`; index avg `0.0125` n `27`; metal avg `0.1118` n `20`; unknown avg `0.6077` n `1264`
- 4h: commodity avg `0.3845` n `13`; crypto_alt avg `-0.1311` n `239`; crypto_major avg `-0.6434` n `8`; equity avg `-0.8007` n `163`; fx avg `0.0306` n `6`; index avg `-0.1085` n `27`; metal avg `-0.0725` n `20`; unknown avg `4.4529` n `1256`
- 24h: commodity avg `0.0213` n `13`; crypto_alt avg `-0.0503` n `239`; crypto_major avg `-0.2973` n `8`; equity avg `-0.0739` n `163`; fx avg `-0.0767` n `6`; index avg `0.0009` n `27`; metal avg `-0.9339` n `20`; unknown avg `9.4125` n `1135`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
