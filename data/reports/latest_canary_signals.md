# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T04:22:24.719229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.0422` n `232`; crypto_major avg `-0.0272` n `8`; equity avg `-0.0135` n `132`; fx avg `-0.0015` n `6`; index avg `-0.0013` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.0527` n `792`
- 1h: commodity avg `-0.0322` n `12`; crypto_alt avg `-0.2993` n `232`; crypto_major avg `-0.2426` n `8`; equity avg `-0.164` n `132`; fx avg `-0.0158` n `6`; index avg `-0.0484` n `26`; metal avg `0.0065` n `20`; unknown avg `-0.2227` n `790`
- 4h: commodity avg `-0.0396` n `12`; crypto_alt avg `0.0884` n `232`; crypto_major avg `-0.2005` n `8`; equity avg `-0.5152` n `132`; fx avg `-0.034` n `6`; index avg `-0.127` n `26`; metal avg `-0.2227` n `20`; unknown avg `0.7023` n `790`
- 24h: commodity avg `0.8116` n `12`; crypto_alt avg `-0.969` n `232`; crypto_major avg `-1.9984` n `8`; equity avg `-2.5878` n `130`; fx avg `-0.0905` n `6`; index avg `-0.471` n `26`; metal avg `-1.0778` n `20`; unknown avg `-0.4667` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0512`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.047`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0358`, n `668`, weak_sample_signal
