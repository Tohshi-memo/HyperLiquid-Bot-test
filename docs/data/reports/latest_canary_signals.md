# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T13:07:38.753834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0776` n `12`; crypto_alt avg `0.0267` n `230`; crypto_major avg `0.021` n `8`; equity avg `0.1334` n `98`; fx avg `-0.0058` n `6`; index avg `0.0241` n `25`; metal avg `-0.0134` n `20`; unknown avg `-0.0658` n `770`
- 1h: commodity avg `0.0396` n `12`; crypto_alt avg `-0.1246` n `230`; crypto_major avg `-0.1763` n `8`; equity avg `0.0161` n `98`; fx avg `-0.0129` n `6`; index avg `0.0099` n `25`; metal avg `-0.0619` n `20`; unknown avg `-0.0001` n `770`
- 4h: commodity avg `0.071` n `12`; crypto_alt avg `0.7589` n `230`; crypto_major avg `0.9086` n `8`; equity avg `0.8324` n `98`; fx avg `-0.0215` n `6`; index avg `0.1421` n `25`; metal avg `-0.0355` n `20`; unknown avg `0.1871` n `770`
- 24h: commodity avg `-0.486` n `12`; crypto_alt avg `0.8077` n `230`; crypto_major avg `0.4759` n `8`; equity avg `0.9739` n `97`; fx avg `-0.0558` n `6`; index avg `0.1933` n `25`; metal avg `0.1367` n `20`; unknown avg `0.0678` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0886`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0785`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
