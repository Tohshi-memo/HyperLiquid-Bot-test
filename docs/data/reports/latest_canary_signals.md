# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T01:52:29.473925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0261` n `12`; crypto_alt avg `-0.4201` n `232`; crypto_major avg `-0.4211` n `8`; equity avg `-0.1563` n `132`; fx avg `0.027` n `6`; index avg `-0.0324` n `26`; metal avg `-0.0627` n `20`; unknown avg `-0.4019` n `792`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `-0.8083` n `232`; crypto_major avg `-0.7375` n `8`; equity avg `-0.3423` n `132`; fx avg `0.0077` n `6`; index avg `-0.0659` n `26`; metal avg `-0.2006` n `20`; unknown avg `-0.1379` n `790`
- 4h: commodity avg `0.2611` n `12`; crypto_alt avg `-0.9382` n `232`; crypto_major avg `-0.7689` n `8`; equity avg `-0.3317` n `132`; fx avg `-0.0418` n `6`; index avg `-0.0576` n `26`; metal avg `-0.3308` n `20`; unknown avg `0.0057` n `790`
- 24h: commodity avg `1.0679` n `12`; crypto_alt avg `-1.9773` n `232`; crypto_major avg `-2.5263` n `8`; equity avg `-2.4647` n `130`; fx avg `-0.0401` n `6`; index avg `-0.4414` n `26`; metal avg `-1.1611` n `20`; unknown avg `0.0142` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0461`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0391`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0385`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0312`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0305`, n `668`, weak_sample_signal
