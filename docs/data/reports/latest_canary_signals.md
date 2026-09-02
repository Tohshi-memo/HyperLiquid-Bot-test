# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T20:52:34.696272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.0326` n `232`; crypto_major avg `0.0221` n `8`; equity avg `-0.0055` n `133`; fx avg `0.0007` n `6`; index avg `0.0018` n `26`; metal avg `0.0098` n `20`; unknown avg `0.1844` n `792`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `0.4039` n `232`; crypto_major avg `0.4045` n `8`; equity avg `-0.1108` n `133`; fx avg `-0.0255` n `6`; index avg `-0.0313` n `26`; metal avg `0.0048` n `20`; unknown avg `0.1696` n `778`
- 4h: commodity avg `0.0223` n `12`; crypto_alt avg `0.2334` n `232`; crypto_major avg `0.4325` n `8`; equity avg `0.6902` n `133`; fx avg `-0.0281` n `6`; index avg `0.0232` n `26`; metal avg `0.1506` n `20`; unknown avg `-0.2748` n `778`
- 24h: commodity avg `0.1279` n `12`; crypto_alt avg `0.0702` n `232`; crypto_major avg `-0.0665` n `8`; equity avg `0.6534` n `133`; fx avg `-0.3908` n `6`; index avg `0.0875` n `26`; metal avg `0.5086` n `20`; unknown avg `0.2984` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0544`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0449`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0419`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
