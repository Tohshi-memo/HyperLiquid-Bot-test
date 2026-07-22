# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T11:22:26.129356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0388` n `12`; crypto_alt avg `-0.0207` n `230`; crypto_major avg `-0.0026` n `8`; equity avg `-0.1141` n `98`; fx avg `0.0039` n `6`; index avg `-0.0187` n `25`; metal avg `0.0496` n `20`; unknown avg `0.2996` n `773`
- 1h: commodity avg `0.1028` n `12`; crypto_alt avg `0.0868` n `230`; crypto_major avg `0.0821` n `8`; equity avg `-0.1205` n `98`; fx avg `-0.0139` n `6`; index avg `-0.0438` n `25`; metal avg `0.0003` n `20`; unknown avg `0.2908` n `773`
- 4h: commodity avg `0.1203` n `12`; crypto_alt avg `0.6139` n `230`; crypto_major avg `0.534` n `8`; equity avg `0.0321` n `98`; fx avg `-0.0257` n `6`; index avg `-0.013` n `25`; metal avg `0.0023` n `20`; unknown avg `0.4221` n `772`
- 24h: commodity avg `0.6112` n `12`; crypto_alt avg `-0.372` n `230`; crypto_major avg `-1.0177` n `8`; equity avg `0.7276` n `98`; fx avg `-0.0144` n `6`; index avg `-0.0093` n `25`; metal avg `0.3963` n `20`; unknown avg `0.4038` n `739`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1037`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0807`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0726`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0696`, n `666`, weak_sample_signal
