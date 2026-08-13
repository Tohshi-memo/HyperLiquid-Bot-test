# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T20:07:29.008203+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.0323` n `230`; crypto_major avg `0.0396` n `8`; equity avg `0.0508` n `113`; fx avg `0.0043` n `6`; index avg `0.0165` n `25`; metal avg `-0.0133` n `20`; unknown avg `0.0359` n `787`
- 1h: commodity avg `0.0279` n `12`; crypto_alt avg `-0.1036` n `230`; crypto_major avg `-0.0854` n `8`; equity avg `-0.389` n `113`; fx avg `0.0095` n `6`; index avg `-0.0388` n `25`; metal avg `-0.0953` n `20`; unknown avg `0.0135` n `787`
- 4h: commodity avg `-0.2991` n `12`; crypto_alt avg `-0.039` n `230`; crypto_major avg `0.2835` n `8`; equity avg `0.1443` n `113`; fx avg `0.0082` n `6`; index avg `0.028` n `25`; metal avg `-0.0799` n `20`; unknown avg `0.1413` n `787`
- 24h: commodity avg `-0.4821` n `12`; crypto_alt avg `-0.3717` n `230`; crypto_major avg `0.3218` n `8`; equity avg `1.202` n `113`; fx avg `0.0075` n `6`; index avg `0.2818` n `25`; metal avg `-0.5583` n `20`; unknown avg `-0.0024` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.24`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2047`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1931`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
