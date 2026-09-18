# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T06:37:28.383603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1134` n `12`; crypto_alt avg `0.0585` n `234`; crypto_major avg `-0.0834` n `8`; equity avg `0.102` n `140`; fx avg `0.0336` n `6`; index avg `0.0321` n `26`; metal avg `0.0167` n `20`; unknown avg `0.1166` n `909`
- 1h: commodity avg `-0.1502` n `12`; crypto_alt avg `0.0934` n `234`; crypto_major avg `-0.0726` n `8`; equity avg `0.256` n `140`; fx avg `-0.0098` n `6`; index avg `0.0419` n `26`; metal avg `0.1303` n `20`; unknown avg `9.7678` n `871`
- 4h: commodity avg `-0.2002` n `12`; crypto_alt avg `1.1355` n `234`; crypto_major avg `1.0521` n `8`; equity avg `0.9702` n `140`; fx avg `0.1163` n `6`; index avg `0.1683` n `26`; metal avg `0.2881` n `20`; unknown avg `5.1621` n `853`
- 24h: commodity avg `-0.2639` n `12`; crypto_alt avg `4.941` n `234`; crypto_major avg `3.6298` n `8`; equity avg `2.4378` n `140`; fx avg `0.1616` n `6`; index avg `0.3521` n `26`; metal avg `0.6585` n `20`; unknown avg `4.771` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
