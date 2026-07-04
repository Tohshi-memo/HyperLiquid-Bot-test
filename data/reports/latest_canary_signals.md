# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T13:07:25.036029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0473` n `12`; crypto_alt avg `-0.1068` n `229`; crypto_major avg `0.0176` n `8`; equity avg `-0.0197` n `88`; fx avg `-0.0` n `6`; index avg `0.0136` n `25`; metal avg `0.0114` n `20`; unknown avg `0.0059` n `759`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.086` n `229`; crypto_major avg `0.0506` n `8`; equity avg `-0.02` n `88`; fx avg `-0.0075` n `6`; index avg `0.0105` n `25`; metal avg `0.0096` n `20`; unknown avg `-0.0623` n `759`
- 4h: commodity avg `0.0917` n `12`; crypto_alt avg `0.4855` n `229`; crypto_major avg `0.014` n `8`; equity avg `-0.0469` n `88`; fx avg `0.0049` n `6`; index avg `0.0096` n `25`; metal avg `0.0168` n `20`; unknown avg `-0.2661` n `759`
- 24h: commodity avg `0.0552` n `12`; crypto_alt avg `0.7639` n `229`; crypto_major avg `1.2818` n `8`; equity avg `0.2419` n `88`; fx avg `-0.0629` n `6`; index avg `-0.0294` n `25`; metal avg `0.0334` n `20`; unknown avg `2.5423` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
