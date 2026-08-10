# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T12:52:36.657662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.0109` n `230`; crypto_major avg `-0.1275` n `8`; equity avg `-0.1562` n `113`; fx avg `0.0095` n `6`; index avg `-0.0133` n `25`; metal avg `0.0243` n `20`; unknown avg `-0.0534` n `784`
- 1h: commodity avg `0.0291` n `12`; crypto_alt avg `-0.1174` n `230`; crypto_major avg `-0.2674` n `8`; equity avg `-0.5288` n `113`; fx avg `-0.0009` n `6`; index avg `-0.0561` n `25`; metal avg `0.027` n `20`; unknown avg `-0.0046` n `784`
- 4h: commodity avg `0.1172` n `12`; crypto_alt avg `-0.0202` n `230`; crypto_major avg `-0.3189` n `8`; equity avg `-0.8999` n `113`; fx avg `-0.0135` n `6`; index avg `-0.1256` n `25`; metal avg `-0.0127` n `20`; unknown avg `-0.1551` n `784`
- 24h: commodity avg `0.6898` n `12`; crypto_alt avg `0.7975` n `230`; crypto_major avg `-0.0381` n `8`; equity avg `-0.9243` n `113`; fx avg `0.2189` n `6`; index avg `-0.0527` n `25`; metal avg `-0.1331` n `20`; unknown avg `56.9707` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
