# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T00:07:25.137470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.2136` n `231`; crypto_major avg `-0.3742` n `8`; equity avg `-0.0381` n `127`; fx avg `0.0001` n `6`; index avg `0.0321` n `26`; metal avg `0.0121` n `20`; unknown avg `0.0264` n `792`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `-0.2559` n `231`; crypto_major avg `-0.3253` n `8`; equity avg `-0.1283` n `127`; fx avg `-0.0068` n `6`; index avg `0.0096` n `26`; metal avg `-0.0508` n `20`; unknown avg `0.0137` n `792`
- 4h: commodity avg `-0.0451` n `12`; crypto_alt avg `0.1496` n `231`; crypto_major avg `-0.06` n `8`; equity avg `-0.5933` n `127`; fx avg `-0.0058` n `6`; index avg `-0.034` n `26`; metal avg `-0.0344` n `20`; unknown avg `-0.1828` n `792`
- 24h: commodity avg `0.3663` n `12`; crypto_alt avg `0.7011` n `231`; crypto_major avg `1.918` n `8`; equity avg `-0.6125` n `127`; fx avg `-0.0152` n `6`; index avg `-0.1027` n `26`; metal avg `0.0409` n `20`; unknown avg `0.8679` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
