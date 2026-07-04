# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T07:22:29.618967+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `12`; crypto_alt avg `0.0252` n `229`; crypto_major avg `0.1459` n `8`; equity avg `-0.013` n `88`; fx avg `-0.0031` n `6`; index avg `-0.0112` n `25`; metal avg `0.0055` n `20`; unknown avg `0.4453` n `765`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `0.1085` n `229`; crypto_major avg `0.1694` n `8`; equity avg `0.0191` n `88`; fx avg `-0.0067` n `6`; index avg `-0.0051` n `25`; metal avg `-0.005` n `20`; unknown avg `0.042` n `765`
- 4h: commodity avg `-0.032` n `12`; crypto_alt avg `-0.2992` n `229`; crypto_major avg `0.0982` n `8`; equity avg `0.0706` n `88`; fx avg `0.0183` n `6`; index avg `0.0092` n `25`; metal avg `0.0132` n `20`; unknown avg `0.1374` n `745`
- 24h: commodity avg `-0.1069` n `12`; crypto_alt avg `1.7789` n `229`; crypto_major avg `2.338` n `8`; equity avg `0.4476` n `88`; fx avg `0.0078` n `6`; index avg `-0.0225` n `25`; metal avg `-0.0787` n `20`; unknown avg `5.269` n `733`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0552`, n `668`, weak_sample_signal
