# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T09:22:25.837720+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.0872` n `229`; crypto_major avg `0.0864` n `8`; equity avg `0.0028` n `88`; fx avg `0.0028` n `6`; index avg `-0.0035` n `25`; metal avg `0.0095` n `20`; unknown avg `-0.1109` n `765`
- 1h: commodity avg `0.0013` n `12`; crypto_alt avg `0.0881` n `229`; crypto_major avg `-0.0602` n `8`; equity avg `-0.0132` n `88`; fx avg `0.0047` n `6`; index avg `0.0016` n `25`; metal avg `0.0136` n `20`; unknown avg `0.0925` n `765`
- 4h: commodity avg `0.0251` n `12`; crypto_alt avg `-0.1559` n `229`; crypto_major avg `-0.0554` n `8`; equity avg `0.0218` n `88`; fx avg `-0.012` n `6`; index avg `0.0155` n `25`; metal avg `0.0354` n `20`; unknown avg `0.6088` n `745`
- 24h: commodity avg `-0.0425` n `12`; crypto_alt avg `1.3151` n `229`; crypto_major avg `2.1645` n `8`; equity avg `0.3198` n `88`; fx avg `-0.0396` n `6`; index avg `-0.0013` n `25`; metal avg `-0.1252` n `20`; unknown avg `5.8275` n `733`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0934`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
