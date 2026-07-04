# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T21:07:31.119461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.0554` n `229`; crypto_major avg `-0.0066` n `8`; equity avg `-0.0037` n `88`; fx avg `0.0043` n `6`; index avg `0.0005` n `25`; metal avg `0.002` n `20`; unknown avg `-0.0422` n `765`
- 1h: commodity avg `-0.0123` n `12`; crypto_alt avg `-0.2133` n `229`; crypto_major avg `-0.2736` n `8`; equity avg `-0.0163` n `88`; fx avg `0.0222` n `6`; index avg `-0.0001` n `25`; metal avg `0.0169` n `20`; unknown avg `-0.1267` n `765`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.2453` n `229`; crypto_major avg `-0.1624` n `8`; equity avg `0.0931` n `88`; fx avg `-0.0269` n `6`; index avg `0.0353` n `25`; metal avg `0.0539` n `20`; unknown avg `-0.9371` n `765`
- 24h: commodity avg `0.0453` n `12`; crypto_alt avg `0.1661` n `229`; crypto_major avg `0.2431` n `8`; equity avg `0.2573` n `88`; fx avg `-0.0248` n `6`; index avg `-0.0201` n `25`; metal avg `0.0859` n `20`; unknown avg `-0.3883` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
