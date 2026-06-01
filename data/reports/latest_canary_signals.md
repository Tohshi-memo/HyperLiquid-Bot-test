# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T03:07:18.093142+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1046` n `12`; crypto_alt avg `0.3324` n `228`; crypto_major avg `0.2589` n `8`; equity avg `0.2258` n `69`; fx avg `-0.0111` n `6`; index avg `0.0311` n `23`; metal avg `0.0157` n `18`; unknown avg `0.6755` n `422`
- 1h: commodity avg `-0.0715` n `12`; crypto_alt avg `1.1412` n `228`; crypto_major avg `0.8008` n `8`; equity avg `0.2126` n `69`; fx avg `0.0229` n `6`; index avg `0.4271` n `23`; metal avg `-0.1876` n `18`; unknown avg `0.1801` n `422`
- 4h: commodity avg `0.2388` n `12`; crypto_alt avg `0.7498` n `228`; crypto_major avg `0.0148` n `8`; equity avg `0.1719` n `69`; fx avg `0.0898` n `6`; index avg `0.2416` n `23`; metal avg `0.2205` n `18`; unknown avg `0.489` n `421`
- 24h: commodity avg `1.0802` n `12`; crypto_alt avg `1.4941` n `228`; crypto_major avg `0.1331` n `8`; equity avg `0.6711` n `69`; fx avg `0.0473` n `6`; index avg `0.6598` n `23`; metal avg `0.2605` n `18`; unknown avg `1.8515` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2852`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2451`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2038`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
