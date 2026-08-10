# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T12:22:30.932823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0316` n `12`; crypto_alt avg `-0.0444` n `230`; crypto_major avg `-0.0653` n `8`; equity avg `-0.2707` n `113`; fx avg `0.0173` n `6`; index avg `-0.0239` n `25`; metal avg `-0.0506` n `20`; unknown avg `0.0538` n `784`
- 1h: commodity avg `0.0838` n `12`; crypto_alt avg `0.1281` n `230`; crypto_major avg `0.1859` n `8`; equity avg `-0.1914` n `113`; fx avg `-0.0071` n `6`; index avg `-0.0251` n `25`; metal avg `0.0097` n `20`; unknown avg `-0.0277` n `784`
- 4h: commodity avg `0.2192` n `12`; crypto_alt avg `0.0661` n `230`; crypto_major avg `-0.0628` n `8`; equity avg `-0.6898` n `113`; fx avg `-0.0065` n `6`; index avg `-0.0973` n `25`; metal avg `-0.126` n `20`; unknown avg `-0.0958` n `784`
- 24h: commodity avg `0.5931` n `12`; crypto_alt avg `1.0019` n `230`; crypto_major avg `0.3104` n `8`; equity avg `-0.6524` n `113`; fx avg `0.2076` n `6`; index avg `-0.0063` n `25`; metal avg `-0.1632` n `20`; unknown avg `57.0632` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1762`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
