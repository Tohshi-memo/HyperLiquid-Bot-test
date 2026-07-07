# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T11:07:28.176186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0734` n `12`; crypto_alt avg `0.0038` n `229`; crypto_major avg `-0.0422` n `8`; equity avg `-0.0603` n `91`; fx avg `-0.0093` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0339` n `20`; unknown avg `-0.0594` n `763`
- 1h: commodity avg `0.1448` n `12`; crypto_alt avg `-0.0413` n `229`; crypto_major avg `-0.4018` n `8`; equity avg `-0.1847` n `91`; fx avg `-0.0463` n `6`; index avg `-0.0936` n `25`; metal avg `-0.08` n `20`; unknown avg `-0.1133` n `763`
- 4h: commodity avg `0.0798` n `12`; crypto_alt avg `-0.1189` n `229`; crypto_major avg `-0.4144` n `8`; equity avg `-0.4739` n `91`; fx avg `-0.1595` n `6`; index avg `-0.1056` n `25`; metal avg `0.136` n `20`; unknown avg `-0.4733` n `757`
- 24h: commodity avg `0.5218` n `12`; crypto_alt avg `0.3964` n `229`; crypto_major avg `-0.3925` n `8`; equity avg `-1.553` n `90`; fx avg `-0.1459` n `6`; index avg `-0.4233` n `25`; metal avg `-0.3066` n `20`; unknown avg `-0.4539` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0494`, n `668`, weak_sample_signal
