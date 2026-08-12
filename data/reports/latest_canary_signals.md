# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T02:37:27.824011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `12`; crypto_alt avg `0.0139` n `230`; crypto_major avg `-0.0143` n `8`; equity avg `0.1965` n `113`; fx avg `0.0001` n `6`; index avg `0.054` n `25`; metal avg `-0.0448` n `20`; unknown avg `0.0882` n `786`
- 1h: commodity avg `0.0078` n `12`; crypto_alt avg `0.1024` n `230`; crypto_major avg `0.0326` n `8`; equity avg `0.449` n `113`; fx avg `0.0194` n `6`; index avg `0.0836` n `25`; metal avg `0.0337` n `20`; unknown avg `-0.0007` n `786`
- 4h: commodity avg `0.089` n `12`; crypto_alt avg `0.2169` n `230`; crypto_major avg `0.0472` n `8`; equity avg `0.796` n `113`; fx avg `0.0348` n `6`; index avg `0.1565` n `25`; metal avg `0.0785` n `20`; unknown avg `-0.1938` n `786`
- 24h: commodity avg `0.2263` n `12`; crypto_alt avg `-1.0819` n `230`; crypto_major avg `0.6926` n `8`; equity avg `1.6768` n `113`; fx avg `0.0051` n `6`; index avg `0.1562` n `25`; metal avg `-0.2314` n `20`; unknown avg `-0.0533` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.225`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2214`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.2056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2055`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
