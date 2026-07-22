# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T04:22:23.242450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `12`; crypto_alt avg `0.0832` n `230`; crypto_major avg `0.0738` n `8`; equity avg `0.0646` n `98`; fx avg `0.0096` n `6`; index avg `0.0016` n `25`; metal avg `-0.0507` n `20`; unknown avg `-0.1027` n `771`
- 1h: commodity avg `-0.0038` n `12`; crypto_alt avg `0.0061` n `230`; crypto_major avg `0.1257` n `8`; equity avg `0.0935` n `98`; fx avg `0.0205` n `6`; index avg `0.0304` n `25`; metal avg `-0.1214` n `20`; unknown avg `-0.3124` n `771`
- 4h: commodity avg `0.088` n `12`; crypto_alt avg `-0.3745` n `230`; crypto_major avg `-0.4253` n `8`; equity avg `-0.7826` n `98`; fx avg `0.0524` n `6`; index avg `-0.0801` n `25`; metal avg `0.2802` n `20`; unknown avg `-0.4597` n `771`
- 24h: commodity avg `0.6258` n `12`; crypto_alt avg `0.1112` n `230`; crypto_major avg `0.0451` n `8`; equity avg `2.3744` n `98`; fx avg `0.1024` n `6`; index avg `0.3045` n `25`; metal avg `0.7833` n `20`; unknown avg `0.2582` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0944`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0601`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0522`, n `666`, weak_sample_signal
