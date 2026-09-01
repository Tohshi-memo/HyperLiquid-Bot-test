# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T19:22:29.779562+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0205` n `12`; crypto_alt avg `0.2226` n `232`; crypto_major avg `0.2181` n `8`; equity avg `0.148` n `131`; fx avg `0.0043` n `6`; index avg `0.0073` n `26`; metal avg `0.0265` n `20`; unknown avg `0.1598` n `793`
- 1h: commodity avg `0.204` n `12`; crypto_alt avg `0.6011` n `232`; crypto_major avg `0.4059` n `8`; equity avg `0.1274` n `131`; fx avg `-0.0098` n `6`; index avg `0.0007` n `26`; metal avg `-0.0668` n `20`; unknown avg `1.1832` n `791`
- 4h: commodity avg `0.5469` n `12`; crypto_alt avg `-0.5757` n `232`; crypto_major avg `-0.7918` n `8`; equity avg `-0.299` n `131`; fx avg `-0.0015` n `6`; index avg `-0.1381` n `26`; metal avg `-0.2636` n `20`; unknown avg `-1.1767` n `790`
- 24h: commodity avg `0.9298` n `12`; crypto_alt avg `-0.2727` n `232`; crypto_major avg `-2.014` n `8`; equity avg `-1.4742` n `130`; fx avg `0.0336` n `6`; index avg `-0.2733` n `26`; metal avg `-0.794` n `20`; unknown avg `0.2978` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0446`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.035`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.034`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0328`, n `668`, weak_sample_signal
