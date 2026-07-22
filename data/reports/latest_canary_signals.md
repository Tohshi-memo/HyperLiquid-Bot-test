# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T20:07:29.691149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0431` n `12`; crypto_alt avg `0.0039` n `230`; crypto_major avg `-0.0356` n `8`; equity avg `-0.2475` n `98`; fx avg `0.0019` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0054` n `20`; unknown avg `-0.0179` n `773`
- 1h: commodity avg `-0.1401` n `12`; crypto_alt avg `-0.0617` n `230`; crypto_major avg `-0.1561` n `8`; equity avg `-0.2955` n `98`; fx avg `-0.0048` n `6`; index avg `-0.0464` n `25`; metal avg `-0.0287` n `20`; unknown avg `0.0033` n `773`
- 4h: commodity avg `0.1214` n `12`; crypto_alt avg `-0.4836` n `230`; crypto_major avg `-0.3517` n `8`; equity avg `-1.0373` n `98`; fx avg `0.0045` n `6`; index avg `-0.1185` n `25`; metal avg `-0.2229` n `20`; unknown avg `0.1605` n `773`
- 24h: commodity avg `0.4347` n `12`; crypto_alt avg `-0.5564` n `230`; crypto_major avg `-0.7758` n `8`; equity avg `-1.1222` n `98`; fx avg `-0.0617` n `6`; index avg `-0.1647` n `25`; metal avg `0.2304` n `20`; unknown avg `1.3977` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0914`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
