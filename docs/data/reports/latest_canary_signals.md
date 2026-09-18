# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T02:52:27.758157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `0.0106` n `234`; crypto_major avg `-0.1533` n `8`; equity avg `0.0441` n `140`; fx avg `-0.0119` n `6`; index avg `0.0058` n `26`; metal avg `0.0268` n `20`; unknown avg `4.5965` n `909`
- 1h: commodity avg `0.0288` n `12`; crypto_alt avg `0.4935` n `234`; crypto_major avg `0.176` n `8`; equity avg `0.2206` n `140`; fx avg `-0.048` n `6`; index avg `0.0309` n `26`; metal avg `0.0774` n `20`; unknown avg `3.5782` n `907`
- 4h: commodity avg `-0.0362` n `12`; crypto_alt avg `2.0479` n `234`; crypto_major avg `1.2986` n `8`; equity avg `0.0865` n `140`; fx avg `0.0563` n `6`; index avg `-0.0578` n `26`; metal avg `0.2129` n `20`; unknown avg `-0.1049` n `901`
- 24h: commodity avg `-0.2761` n `12`; crypto_alt avg `4.5357` n `234`; crypto_major avg `2.4961` n `8`; equity avg `1.5555` n `140`; fx avg `0.0413` n `6`; index avg `0.2011` n `26`; metal avg `0.566` n `20`; unknown avg `1.45` n `757`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
