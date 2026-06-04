# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T23:41:03.540702+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0685` n `12`; crypto_alt avg `0.4701` n `228`; crypto_major avg `0.6118` n `8`; equity avg `0.0149` n `74`; fx avg `-0.0065` n `6`; index avg `0.0016` n `23`; metal avg `-0.0879` n `18`; unknown avg `0.0772` n `424`
- 1h: commodity avg `0.0164` n `12`; crypto_alt avg `0.7618` n `228`; crypto_major avg `0.7446` n `8`; equity avg `-0.165` n `74`; fx avg `-0.002` n `6`; index avg `-0.1315` n `23`; metal avg `-0.1919` n `18`; unknown avg `0.081` n `424`
- 4h: commodity avg `-0.0089` n `12`; crypto_alt avg `-2.1622` n `228`; crypto_major avg `-0.9538` n `8`; equity avg `-1.2166` n `74`; fx avg `0.0036` n `6`; index avg `-0.4593` n `23`; metal avg `-0.3169` n `18`; unknown avg `-0.9935` n `424`
- 24h: commodity avg `-0.5036` n `12`; crypto_alt avg `-6.4188` n `228`; crypto_major avg `-3.9152` n `8`; equity avg `-0.1834` n `73`; fx avg `0.0531` n `6`; index avg `0.1524` n `23`; metal avg `0.4732` n `18`; unknown avg `-1.5145` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
