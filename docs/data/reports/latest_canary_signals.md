# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T13:07:27.479459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0613` n `12`; crypto_alt avg `0.0064` n `230`; crypto_major avg `0.0001` n `8`; equity avg `0.0302` n `114`; fx avg `0.0103` n `6`; index avg `0.0152` n `25`; metal avg `0.014` n `20`; unknown avg `0.0679` n `792`
- 1h: commodity avg `0.0877` n `12`; crypto_alt avg `-0.1091` n `230`; crypto_major avg `-0.2558` n `8`; equity avg `-0.2219` n `114`; fx avg `0.0112` n `6`; index avg `-0.0241` n `25`; metal avg `-0.0247` n `20`; unknown avg `0.0235` n `792`
- 4h: commodity avg `0.0559` n `12`; crypto_alt avg `0.0568` n `230`; crypto_major avg `-0.0055` n `8`; equity avg `-0.3758` n `114`; fx avg `0.0282` n `6`; index avg `-0.0295` n `25`; metal avg `-0.0449` n `20`; unknown avg `1.6474` n `792`
- 24h: commodity avg `-0.0424` n `12`; crypto_alt avg `-0.2375` n `230`; crypto_major avg `0.5344` n `8`; equity avg `0.9521` n `114`; fx avg `-0.0018` n `6`; index avg `0.1078` n `25`; metal avg `0.1061` n `20`; unknown avg `0.0123` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
