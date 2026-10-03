# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T18:07:36.657326+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `13`; crypto_alt avg `-0.0516` n `235`; crypto_major avg `0.0511` n `8`; equity avg `0.0152` n `143`; fx avg `-0.0012` n `6`; index avg `-0.0046` n `26`; metal avg `0.0016` n `20`; unknown avg `0.3508` n `1076`
- 1h: commodity avg `-0.1262` n `13`; crypto_alt avg `0.0004` n `235`; crypto_major avg `0.176` n `8`; equity avg `0.0308` n `143`; fx avg `-0.0085` n `6`; index avg `0.0018` n `26`; metal avg `-0.004` n `20`; unknown avg `0.3865` n `1076`
- 4h: commodity avg `0.0074` n `13`; crypto_alt avg `0.7198` n `235`; crypto_major avg `0.6636` n `8`; equity avg `0.1144` n `143`; fx avg `-0.0137` n `6`; index avg `0.02` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.2305` n `966`
- 24h: commodity avg `0.088` n `13`; crypto_alt avg `0.3703` n `235`; crypto_major avg `0.1693` n `8`; equity avg `0.2248` n `143`; fx avg `-0.0507` n `6`; index avg `0.057` n `26`; metal avg `0.0902` n `20`; unknown avg `-0.1487` n `868`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1871`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
