# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T04:07:29.179638+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.0657` n `230`; crypto_major avg `-0.022` n `8`; equity avg `0.0079` n `98`; fx avg `-0.0029` n `6`; index avg `0.0358` n `25`; metal avg `0.018` n `20`; unknown avg `-0.0665` n `771`
- 1h: commodity avg `-0.0298` n `12`; crypto_alt avg `-0.2324` n `230`; crypto_major avg `-0.0726` n `8`; equity avg `-0.0282` n `98`; fx avg `0.0008` n `6`; index avg `-0.0041` n `25`; metal avg `-0.0547` n `20`; unknown avg `-0.2263` n `771`
- 4h: commodity avg `0.08` n `12`; crypto_alt avg `-0.324` n `230`; crypto_major avg `-0.346` n `8`; equity avg `-0.8768` n `98`; fx avg `0.0337` n `6`; index avg `-0.0959` n `25`; metal avg `0.3702` n `20`; unknown avg `-0.355` n `771`
- 24h: commodity avg `0.6111` n `12`; crypto_alt avg `-0.1693` n `230`; crypto_major avg `-0.2627` n `8`; equity avg `2.2416` n `98`; fx avg `0.0974` n `6`; index avg `0.2917` n `25`; metal avg `0.8015` n `20`; unknown avg `0.3` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0951`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0604`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.053`, n `666`, weak_sample_signal
