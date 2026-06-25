# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T22:10:01.483784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `12`; crypto_alt avg `-0.0661` n `228`; crypto_major avg `-0.1252` n `8`; equity avg `-0.2` n `86`; fx avg `-0.0136` n `6`; index avg `-0.0452` n `23`; metal avg `-0.0991` n `20`; unknown avg `-0.3842` n `765`
- 1h: commodity avg `0.0598` n `12`; crypto_alt avg `0.7194` n `228`; crypto_major avg `0.8029` n `8`; equity avg `-0.2358` n `86`; fx avg `-0.0101` n `6`; index avg `-0.0579` n `23`; metal avg `-0.0521` n `20`; unknown avg `0.6925` n `765`
- 4h: commodity avg `-0.1587` n `12`; crypto_alt avg `0.3607` n `228`; crypto_major avg `0.307` n `8`; equity avg `-0.1858` n `86`; fx avg `-0.0202` n `6`; index avg `-0.0469` n `23`; metal avg `-0.1263` n `20`; unknown avg `0.6949` n `765`
- 24h: commodity avg `0.435` n `12`; crypto_alt avg `-1.4867` n `228`; crypto_major avg `-1.3976` n `8`; equity avg `-2.3652` n `86`; fx avg `0.1351` n `6`; index avg `-0.2123` n `23`; metal avg `0.2238` n `20`; unknown avg `0.685` n `700`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
