# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T10:07:33.676263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0629` n `13`; crypto_alt avg `-0.1247` n `235`; crypto_major avg `-0.186` n `8`; equity avg `-0.1155` n `151`; fx avg `0.0045` n `6`; index avg `-0.0217` n `26`; metal avg `-0.0206` n `20`; unknown avg `0.041` n `1133`
- 1h: commodity avg `0.1626` n `13`; crypto_alt avg `-0.5029` n `235`; crypto_major avg `-0.3764` n `8`; equity avg `-0.0915` n `151`; fx avg `0.0021` n `6`; index avg `-0.01` n `26`; metal avg `0.0068` n `20`; unknown avg `0.0535` n `1133`
- 4h: commodity avg `0.0747` n `13`; crypto_alt avg `-0.6704` n `235`; crypto_major avg `-0.4645` n `8`; equity avg `-0.002` n `151`; fx avg `-0.0488` n `6`; index avg `0.0821` n `26`; metal avg `-0.0732` n `20`; unknown avg `1192.5707` n `1037`
- 24h: commodity avg `1.2839` n `13`; crypto_alt avg `-0.8435` n `235`; crypto_major avg `-0.5078` n `8`; equity avg `-0.5604` n `151`; fx avg `0.0508` n `6`; index avg `-0.0372` n `26`; metal avg `-0.4884` n `20`; unknown avg `1267.9306` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1518`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1309`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1141`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0738`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0738`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
