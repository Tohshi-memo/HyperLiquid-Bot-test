# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T17:42:27.746420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `0.1102` n `231`; crypto_major avg `0.1586` n `8`; equity avg `-0.0347` n `122`; fx avg `0.0005` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.0987` n `795`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.2476` n `231`; crypto_major avg `-0.0763` n `8`; equity avg `-0.1619` n `122`; fx avg `0.0045` n `6`; index avg `-0.0365` n `25`; metal avg `-0.0118` n `20`; unknown avg `-0.1496` n `795`
- 4h: commodity avg `0.125` n `12`; crypto_alt avg `-0.2404` n `231`; crypto_major avg `0.1552` n `8`; equity avg `0.05` n `122`; fx avg `-0.02` n `6`; index avg `-0.0783` n `25`; metal avg `0.2853` n `20`; unknown avg `-0.1313` n `795`
- 24h: commodity avg `-0.5781` n `12`; crypto_alt avg `-0.128` n `231`; crypto_major avg `1.0779` n `8`; equity avg `1.6949` n `122`; fx avg `0.0543` n `6`; index avg `0.2085` n `25`; metal avg `-0.0726` n `20`; unknown avg `-0.6744` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
