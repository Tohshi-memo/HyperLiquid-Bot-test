# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T01:07:30.856841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1238` n `12`; crypto_alt avg `-0.0131` n `230`; crypto_major avg `-0.0263` n `8`; equity avg `-0.0446` n `98`; fx avg `-0.0019` n `6`; index avg `0.0167` n `25`; metal avg `0.2143` n `20`; unknown avg `-0.0741` n `771`
- 1h: commodity avg `0.1218` n `12`; crypto_alt avg `0.0996` n `230`; crypto_major avg `0.1103` n `8`; equity avg `-0.2843` n `98`; fx avg `-0.0024` n `6`; index avg `-0.05` n `25`; metal avg `0.2336` n `20`; unknown avg `-0.0481` n `771`
- 4h: commodity avg `0.1172` n `12`; crypto_alt avg `0.2132` n `230`; crypto_major avg `0.3996` n `8`; equity avg `0.0772` n `98`; fx avg `0.0009` n `6`; index avg `0.0314` n `25`; metal avg `0.3097` n `20`; unknown avg `-0.0668` n `771`
- 24h: commodity avg `0.6711` n `12`; crypto_alt avg `0.6821` n `230`; crypto_major avg `0.6517` n `8`; equity avg `3.8799` n `98`; fx avg `0.0102` n `6`; index avg `0.5656` n `25`; metal avg `0.9038` n `20`; unknown avg `0.3913` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0964`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.058`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.057`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0509`, n `666`, weak_sample_signal
