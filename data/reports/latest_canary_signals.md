# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T14:37:33.229660+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `12`; crypto_alt avg `-0.3116` n `232`; crypto_major avg `-0.288` n `8`; equity avg `0.0041` n `134`; fx avg `-0.0118` n `6`; index avg `0.001` n `26`; metal avg `-0.0018` n `20`; unknown avg `-0.034` n `796`
- 1h: commodity avg `0.033` n `12`; crypto_alt avg `-0.4421` n `232`; crypto_major avg `-0.6242` n `8`; equity avg `-0.0314` n `134`; fx avg `-0.0361` n `6`; index avg `-0.0019` n `26`; metal avg `0.0718` n `20`; unknown avg `0.6845` n `794`
- 4h: commodity avg `0.2407` n `12`; crypto_alt avg `0.3651` n `232`; crypto_major avg `-0.3751` n `8`; equity avg `-0.0684` n `134`; fx avg `-0.0211` n `6`; index avg `-0.0138` n `26`; metal avg `0.0937` n `20`; unknown avg `6683.8448` n `748`
- 24h: commodity avg `0.1772` n `12`; crypto_alt avg `1.308` n `232`; crypto_major avg `-0.5775` n `8`; equity avg `0.4574` n `134`; fx avg `-0.1225` n `6`; index avg `0.0505` n `26`; metal avg `-0.0269` n `20`; unknown avg `1.2839` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
