# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T08:37:25.081000+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0457` n `12`; crypto_alt avg `-0.0698` n `230`; crypto_major avg `0.0389` n `8`; equity avg `0.0837` n `114`; fx avg `-0.0044` n `6`; index avg `0.0002` n `25`; metal avg `-0.0072` n `20`; unknown avg `-0.0018` n `792`
- 1h: commodity avg `0.1255` n `12`; crypto_alt avg `-0.2692` n `230`; crypto_major avg `-0.2802` n `8`; equity avg `0.1463` n `114`; fx avg `-0.0065` n `6`; index avg `0.0009` n `25`; metal avg `-0.1105` n `20`; unknown avg `0.0043` n `792`
- 4h: commodity avg `-0.0215` n `12`; crypto_alt avg `-0.2837` n `230`; crypto_major avg `-0.0268` n `8`; equity avg `0.6203` n `114`; fx avg `0.012` n `6`; index avg `0.0729` n `25`; metal avg `0.0515` n `20`; unknown avg `0.0048` n `776`
- 24h: commodity avg `-0.1581` n `12`; crypto_alt avg `-0.1138` n `230`; crypto_major avg `0.5553` n `8`; equity avg `1.3298` n `114`; fx avg `-0.0243` n `6`; index avg `0.1461` n `25`; metal avg `0.2055` n `20`; unknown avg `0.1522` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
