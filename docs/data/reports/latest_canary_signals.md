# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T20:07:38.059957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0067` n `13`; crypto_alt avg `0.1244` n `237`; crypto_major avg `0.157` n `8`; equity avg `-0.0559` n `151`; fx avg `0.0042` n `6`; index avg `0.0037` n `26`; metal avg `-0.0175` n `20`; unknown avg `5.5527` n `1162`
- 1h: commodity avg `0.0307` n `13`; crypto_alt avg `0.1068` n `237`; crypto_major avg `0.0801` n `8`; equity avg `-0.064` n `151`; fx avg `0.0013` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0397` n `20`; unknown avg `-0.267` n `1162`
- 4h: commodity avg `-0.1307` n `13`; crypto_alt avg `0.0018` n `237`; crypto_major avg `-0.0076` n `8`; equity avg `-0.7869` n `151`; fx avg `0.0175` n `6`; index avg `-0.1021` n `26`; metal avg `0.0026` n `20`; unknown avg `-0.1493` n `1162`
- 24h: commodity avg `-0.2917` n `13`; crypto_alt avg `3.0527` n `237`; crypto_major avg `2.2742` n `8`; equity avg `2.8796` n `151`; fx avg `0.0125` n `6`; index avg `0.5678` n `26`; metal avg `0.1107` n `20`; unknown avg `3.0016` n `908`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
