# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T19:07:26.764398+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.1688` n `232`; crypto_major avg `0.2249` n `8`; equity avg `0.1877` n `131`; fx avg `-0.0108` n `6`; index avg `0.0512` n `26`; metal avg `-0.0199` n `20`; unknown avg `0.2753` n `791`
- 1h: commodity avg `0.1344` n `12`; crypto_alt avg `-0.0981` n `232`; crypto_major avg `-0.2294` n `8`; equity avg `-0.1482` n `131`; fx avg `-0.0151` n `6`; index avg `-0.0203` n `26`; metal avg `-0.1093` n `20`; unknown avg `0.8231` n `791`
- 4h: commodity avg `0.5819` n `12`; crypto_alt avg `-0.77` n `232`; crypto_major avg `-0.8837` n `8`; equity avg `-0.5152` n `131`; fx avg `-0.012` n `6`; index avg `-0.1433` n `26`; metal avg `-0.2629` n `20`; unknown avg `0.0275` n `790`
- 24h: commodity avg `0.8941` n `12`; crypto_alt avg `-0.739` n `232`; crypto_major avg `-2.4143` n `8`; equity avg `-1.5777` n `130`; fx avg `0.0256` n `6`; index avg `-0.2615` n `26`; metal avg `-0.7924` n `20`; unknown avg `-0.1865` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0404`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0358`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0354`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.032`, n `668`, weak_sample_signal
