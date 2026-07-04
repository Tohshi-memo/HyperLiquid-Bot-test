# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T08:37:25.628939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `12`; crypto_alt avg `0.1485` n `229`; crypto_major avg `0.0931` n `8`; equity avg `0.0321` n `88`; fx avg `0.0049` n `6`; index avg `0.0024` n `25`; metal avg `0.0009` n `20`; unknown avg `0.3707` n `765`
- 1h: commodity avg `-0.0068` n `12`; crypto_alt avg `0.1797` n `229`; crypto_major avg `0.3073` n `8`; equity avg `0.0883` n `88`; fx avg `0.0031` n `6`; index avg `0.0315` n `25`; metal avg `0.0073` n `20`; unknown avg `0.4832` n `765`
- 4h: commodity avg `0.0163` n `12`; crypto_alt avg `-0.3882` n `229`; crypto_major avg `-0.3625` n `8`; equity avg `0.0205` n `88`; fx avg `-0.0119` n `6`; index avg `0.0053` n `25`; metal avg `0.0137` n `20`; unknown avg `0.7988` n `745`
- 24h: commodity avg `0.0505` n `12`; crypto_alt avg `1.4788` n `229`; crypto_major avg `2.4088` n `8`; equity avg `0.4287` n `88`; fx avg `-0.0416` n `6`; index avg `-0.0228` n `25`; metal avg `-0.2089` n `20`; unknown avg `5.876` n `733`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
