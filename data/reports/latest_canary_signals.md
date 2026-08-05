# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T02:52:28.280977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0431` n `12`; crypto_alt avg `0.0145` n `230`; crypto_major avg `0.0377` n `8`; equity avg `0.0536` n `108`; fx avg `0.0008` n `6`; index avg `0.0032` n `25`; metal avg `0.0556` n `20`; unknown avg `-0.1738` n `781`
- 1h: commodity avg `-0.2816` n `12`; crypto_alt avg `0.2328` n `230`; crypto_major avg `0.3609` n `8`; equity avg `-0.0502` n `108`; fx avg `-0.0126` n `6`; index avg `-0.0269` n `25`; metal avg `0.3142` n `20`; unknown avg `-0.1981` n `781`
- 4h: commodity avg `-0.1135` n `12`; crypto_alt avg `0.3648` n `230`; crypto_major avg `0.5084` n `8`; equity avg `0.5923` n `108`; fx avg `-0.0858` n `6`; index avg `0.0533` n `25`; metal avg `0.3601` n `20`; unknown avg `-0.3044` n `781`
- 24h: commodity avg `-1.5227` n `12`; crypto_alt avg `0.2408` n `230`; crypto_major avg `0.8247` n `8`; equity avg `3.8812` n `107`; fx avg `0.0161` n `6`; index avg `0.7933` n `25`; metal avg `1.059` n `20`; unknown avg `0.3883` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
