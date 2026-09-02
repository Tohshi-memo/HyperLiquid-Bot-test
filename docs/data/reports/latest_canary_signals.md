# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T05:52:31.912670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0715` n `232`; crypto_major avg `0.0879` n `8`; equity avg `0.0244` n `132`; fx avg `-0.0148` n `6`; index avg `0.0029` n `26`; metal avg `0.0213` n `20`; unknown avg `0.8957` n `792`
- 1h: commodity avg `0.0281` n `12`; crypto_alt avg `0.2881` n `232`; crypto_major avg `0.2755` n `8`; equity avg `0.2247` n `132`; fx avg `-0.0306` n `6`; index avg `0.0371` n `26`; metal avg `0.1672` n `20`; unknown avg `0.1121` n `790`
- 4h: commodity avg `-0.1901` n `12`; crypto_alt avg `1.9514` n `232`; crypto_major avg `1.3792` n `8`; equity avg `0.284` n `132`; fx avg `-0.0943` n `6`; index avg `0.0158` n `26`; metal avg `0.2453` n `20`; unknown avg `1.3856` n `790`
- 24h: commodity avg `0.8941` n `12`; crypto_alt avg `-0.8147` n `232`; crypto_major avg `-1.8947` n `8`; equity avg `-2.4979` n `130`; fx avg `-0.1151` n `6`; index avg `-0.4765` n `26`; metal avg `-0.9772` n `20`; unknown avg `-0.2903` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0557`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0469`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
