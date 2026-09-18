# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T11:52:27.290192+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `12`; crypto_alt avg `-0.0362` n `234`; crypto_major avg `-0.1041` n `8`; equity avg `-0.071` n `140`; fx avg `-0.0068` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0474` n `20`; unknown avg `-0.0405` n `928`
- 1h: commodity avg `0.0312` n `12`; crypto_alt avg `-0.6224` n `234`; crypto_major avg `-0.5446` n `8`; equity avg `-0.3087` n `140`; fx avg `-0.0206` n `6`; index avg `-0.0499` n `26`; metal avg `0.0135` n `20`; unknown avg `0.7382` n `923`
- 4h: commodity avg `0.1109` n `12`; crypto_alt avg `0.1033` n `234`; crypto_major avg `0.3204` n `8`; equity avg `-0.42` n `140`; fx avg `0.0191` n `6`; index avg `-0.1012` n `26`; metal avg `-0.0901` n `20`; unknown avg `0.5188` n `917`
- 24h: commodity avg `-0.0517` n `12`; crypto_alt avg `5.5022` n `234`; crypto_major avg `4.6619` n `8`; equity avg `1.4755` n `140`; fx avg `0.1927` n `6`; index avg `0.1658` n `26`; metal avg `0.5681` n `20`; unknown avg `1.8926` n `729`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
