# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T00:22:26.520124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `13`; crypto_alt avg `0.0653` n `236`; crypto_major avg `0.1167` n `8`; equity avg `0.0026` n `151`; fx avg `-0.0007` n `6`; index avg `0.0011` n `26`; metal avg `0.0073` n `20`; unknown avg `0.1072` n `1193`
- 1h: commodity avg `-0.0317` n `13`; crypto_alt avg `0.1771` n `236`; crypto_major avg `0.2153` n `8`; equity avg `-0.0032` n `151`; fx avg `0.0008` n `6`; index avg `-0.0082` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.2246` n `1185`
- 4h: commodity avg `-0.0206` n `13`; crypto_alt avg `-0.7719` n `236`; crypto_major avg `-0.5527` n `8`; equity avg `-0.8289` n `151`; fx avg `0.0059` n `6`; index avg `-0.1123` n `26`; metal avg `-0.0442` n `20`; unknown avg `1.7672` n `1179`
- 24h: commodity avg `-0.2392` n `13`; crypto_alt avg `-2.2215` n `236`; crypto_major avg `-0.9319` n `8`; equity avg `-0.7991` n `151`; fx avg `-0.0349` n `6`; index avg `-0.1078` n `26`; metal avg `-0.0819` n `20`; unknown avg `4.4846` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1633`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1349`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0733`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
