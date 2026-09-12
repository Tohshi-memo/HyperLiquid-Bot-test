# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T04:22:25.979044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.89` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0508` n `12`; crypto_alt avg `-0.0197` n `233`; crypto_major avg `-0.0589` n `8`; equity avg `-0.0212` n `136`; fx avg `-0.002` n `6`; index avg `-0.0004` n `26`; metal avg `-0.0004` n `20`; unknown avg `14.5264` n `838`
- 1h: commodity avg `-0.0767` n `12`; crypto_alt avg `-0.0157` n `233`; crypto_major avg `0.0071` n `8`; equity avg `-0.054` n `136`; fx avg `0.002` n `6`; index avg `0.0024` n `26`; metal avg `-0.0132` n `20`; unknown avg `5.6676` n `824`
- 4h: commodity avg `-0.1594` n `12`; crypto_alt avg `0.4706` n `233`; crypto_major avg `0.0058` n `8`; equity avg `-0.0556` n `136`; fx avg `0.0138` n `6`; index avg `0.0018` n `26`; metal avg `-0.0424` n `20`; unknown avg `1.8019` n `814`
- 24h: commodity avg `-0.6738` n `12`; crypto_alt avg `0.8136` n `233`; crypto_major avg `1.0585` n `8`; equity avg `1.0372` n `136`; fx avg `-0.0991` n `6`; index avg `0.3051` n `26`; metal avg `0.1828` n `20`; unknown avg `11.8017` n `690`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
