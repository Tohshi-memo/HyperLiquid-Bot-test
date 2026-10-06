# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T17:52:32.730630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0402` n `13`; crypto_alt avg `0.0022` n `235`; crypto_major avg `0.0695` n `8`; equity avg `0.0637` n `150`; fx avg `0.0028` n `6`; index avg `0.0021` n `26`; metal avg `0.0231` n `20`; unknown avg `0.0078` n `1076`
- 1h: commodity avg `0.0765` n `13`; crypto_alt avg `-0.0053` n `235`; crypto_major avg `-0.1037` n `8`; equity avg `0.1256` n `150`; fx avg `0.0161` n `6`; index avg `-0.0093` n `26`; metal avg `0.0661` n `20`; unknown avg `-0.1966` n `1074`
- 4h: commodity avg `0.3114` n `13`; crypto_alt avg `-0.4179` n `235`; crypto_major avg `-0.741` n `8`; equity avg `0.0305` n `150`; fx avg `0.0319` n `6`; index avg `-0.0425` n `26`; metal avg `0.153` n `20`; unknown avg `5.7243` n `1018`
- 24h: commodity avg `-0.0405` n `13`; crypto_alt avg `0.1228` n `235`; crypto_major avg `-0.1281` n `8`; equity avg `0.7412` n `149`; fx avg `0.1249` n `6`; index avg `0.0588` n `26`; metal avg `0.0646` n `20`; unknown avg `382.0146` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1661`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
