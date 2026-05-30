# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T16:52:19.226783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.036` n `228`; crypto_major avg `-0.1738` n `8`; equity avg `-0.0109` n `69`; fx avg `0.0007` n `6`; index avg `-0.0244` n `23`; metal avg `-0.0046` n `18`; unknown avg `-0.0969` n `421`
- 1h: commodity avg `-0.3402` n `12`; crypto_alt avg `0.1916` n `228`; crypto_major avg `0.1453` n `8`; equity avg `-0.1642` n `69`; fx avg `-0.0115` n `6`; index avg `-0.0715` n `23`; metal avg `0.0066` n `18`; unknown avg `0.8545` n `421`
- 4h: commodity avg `-0.2839` n `12`; crypto_alt avg `0.3668` n `228`; crypto_major avg `0.7249` n `8`; equity avg `-0.0269` n `69`; fx avg `-0.0027` n `6`; index avg `-0.0314` n `23`; metal avg `0.0064` n `18`; unknown avg `1.0187` n `421`
- 24h: commodity avg `0.1553` n `12`; crypto_alt avg `0.6859` n `228`; crypto_major avg `1.3687` n `8`; equity avg `0.8005` n `69`; fx avg `0.0075` n `6`; index avg `0.1355` n `23`; metal avg `-0.1673` n `18`; unknown avg `1.1039` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1917`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
