# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T08:07:28.633285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.0837` n `237`; crypto_major avg `-0.006` n `8`; equity avg `0.0258` n `151`; fx avg `-0.002` n `6`; index avg `0.0006` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.0799` n `1175`
- 1h: commodity avg `-0.0007` n `13`; crypto_alt avg `-0.2747` n `237`; crypto_major avg `-0.1818` n `8`; equity avg `0.0045` n `151`; fx avg `0.0127` n `6`; index avg `-0.0037` n `26`; metal avg `-0.008` n `20`; unknown avg `0.0532` n `1173`
- 4h: commodity avg `-0.0452` n `13`; crypto_alt avg `-0.8748` n `237`; crypto_major avg `-0.5606` n `8`; equity avg `0.0656` n `151`; fx avg `0.0074` n `6`; index avg `0.0316` n `26`; metal avg `-0.0163` n `20`; unknown avg `0.1934` n `1157`
- 24h: commodity avg `0.0885` n `13`; crypto_alt avg `-2.7796` n `236`; crypto_major avg `-1.0758` n `8`; equity avg `-0.7817` n `151`; fx avg `-0.0396` n `6`; index avg `-0.1009` n `26`; metal avg `-0.0635` n `20`; unknown avg `4.4861` n `1055`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1719`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1327`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0825`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
