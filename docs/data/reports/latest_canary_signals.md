# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T21:07:35.923601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.1786` n `228`; crypto_major avg `0.136` n `8`; equity avg `-0.0144` n `86`; fx avg `-0.0067` n `6`; index avg `0.0191` n `23`; metal avg `0.0084` n `20`; unknown avg `0.0436` n `765`
- 1h: commodity avg `-0.1587` n `12`; crypto_alt avg `0.1135` n `228`; crypto_major avg `-0.3475` n `8`; equity avg `-0.0924` n `86`; fx avg `-0.0054` n `6`; index avg `-0.0213` n `23`; metal avg `-0.0511` n `20`; unknown avg `0.6442` n `765`
- 4h: commodity avg `-0.0541` n `12`; crypto_alt avg `0.4756` n `228`; crypto_major avg `0.6584` n `8`; equity avg `0.2889` n `86`; fx avg `0.0077` n `6`; index avg `0.0416` n `23`; metal avg `-0.1554` n `20`; unknown avg `0.3735` n `765`
- 24h: commodity avg `0.3314` n `12`; crypto_alt avg `-1.216` n `228`; crypto_major avg `-1.443` n `8`; equity avg `-1.978` n `86`; fx avg `0.0737` n `6`; index avg `-0.1091` n `23`; metal avg `0.3081` n `20`; unknown avg `0.6283` n `700`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
