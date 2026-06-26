# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T01:07:32.747881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0548` n `12`; crypto_alt avg `-0.3024` n `228`; crypto_major avg `-0.4969` n `8`; equity avg `-0.4027` n `86`; fx avg `0.0166` n `6`; index avg `-0.0587` n `23`; metal avg `-0.1427` n `20`; unknown avg `0.4445` n `765`
- 1h: commodity avg `0.0232` n `12`; crypto_alt avg `-0.3854` n `228`; crypto_major avg `-0.6454` n `8`; equity avg `-0.7362` n `86`; fx avg `0.0503` n `6`; index avg `-0.1568` n `23`; metal avg `-0.0017` n `20`; unknown avg `2.0443` n `765`
- 4h: commodity avg `0.0541` n `12`; crypto_alt avg `0.4768` n `228`; crypto_major avg `0.4552` n `8`; equity avg `-0.8801` n `86`; fx avg `0.0397` n `6`; index avg `-0.1838` n `23`; metal avg `-0.1523` n `20`; unknown avg `0.0344` n `749`
- 24h: commodity avg `0.3959` n `12`; crypto_alt avg `-1.2769` n `228`; crypto_major avg `-1.4804` n `8`; equity avg `-2.5672` n `86`; fx avg `0.072` n `6`; index avg `-0.2102` n `23`; metal avg `0.2298` n `20`; unknown avg `0.5905` n `700`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
