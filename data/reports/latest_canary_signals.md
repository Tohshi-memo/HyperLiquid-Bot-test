# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T22:37:26.064218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0027` n `12`; crypto_alt avg `0.1102` n `228`; crypto_major avg `0.2229` n `8`; equity avg `-0.0629` n `86`; fx avg `-0.0027` n `6`; index avg `-0.0021` n `23`; metal avg `0.1193` n `20`; unknown avg `0.4696` n `765`
- 1h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.1292` n `228`; crypto_major avg `-0.132` n `8`; equity avg `-0.3713` n `86`; fx avg `-0.0038` n `6`; index avg `-0.033` n `23`; metal avg `-0.0118` n `20`; unknown avg `-0.2034` n `765`
- 4h: commodity avg `-0.1128` n `12`; crypto_alt avg `1.0137` n `228`; crypto_major avg `0.9366` n `8`; equity avg `-0.2174` n `86`; fx avg `-0.0188` n `6`; index avg `-0.045` n `23`; metal avg `-0.0725` n `20`; unknown avg `0.8205` n `765`
- 24h: commodity avg `0.4065` n `12`; crypto_alt avg `-1.2824` n `228`; crypto_major avg `-1.2658` n `8`; equity avg `-2.6268` n `86`; fx avg `0.1012` n `6`; index avg `-0.2412` n `23`; metal avg `0.2452` n `20`; unknown avg `0.8801` n `700`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
