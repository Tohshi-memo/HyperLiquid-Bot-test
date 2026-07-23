# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T00:07:27.911622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0547` n `12`; crypto_alt avg `0.1161` n `230`; crypto_major avg `0.2017` n `8`; equity avg `0.1646` n `98`; fx avg `0.0119` n `6`; index avg `0.046` n `25`; metal avg `0.0305` n `20`; unknown avg `-0.0461` n `773`
- 1h: commodity avg `0.0238` n `12`; crypto_alt avg `0.0287` n `230`; crypto_major avg `0.1803` n `8`; equity avg `0.4224` n `98`; fx avg `0.0219` n `6`; index avg `0.1279` n `25`; metal avg `0.1194` n `20`; unknown avg `0.035` n `773`
- 4h: commodity avg `0.2933` n `12`; crypto_alt avg `0.1266` n `230`; crypto_major avg `0.4738` n `8`; equity avg `0.6524` n `98`; fx avg `0.004` n `6`; index avg `0.0898` n `25`; metal avg `-0.0088` n `20`; unknown avg `0.1631` n `773`
- 24h: commodity avg `0.7394` n `12`; crypto_alt avg `-0.5573` n `230`; crypto_major avg `-0.559` n `8`; equity avg `-1.2149` n `98`; fx avg `-0.0409` n `6`; index avg `-0.1695` n `25`; metal avg `0.1676` n `20`; unknown avg `1.6424` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0888`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.074`, n `666`, weak_sample_signal
