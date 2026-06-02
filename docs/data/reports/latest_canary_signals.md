# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T03:37:21.825717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1055` n `12`; crypto_alt avg `0.2903` n `228`; crypto_major avg `0.0143` n `8`; equity avg `0.1327` n `69`; fx avg `0.0035` n `6`; index avg `0.0086` n `23`; metal avg `0.14` n `18`; unknown avg `1.9773` n `422`
- 1h: commodity avg `-0.118` n `12`; crypto_alt avg `0.8269` n `228`; crypto_major avg `0.267` n `8`; equity avg `0.0859` n `69`; fx avg `0.0169` n `6`; index avg `-0.0405` n `23`; metal avg `0.216` n `18`; unknown avg `-0.1831` n `422`
- 4h: commodity avg `-0.4325` n `12`; crypto_alt avg `-0.1709` n `228`; crypto_major avg `-0.1555` n `8`; equity avg `-0.4409` n `69`; fx avg `0.0605` n `6`; index avg `-0.5621` n `23`; metal avg `0.2635` n `18`; unknown avg `-0.2015` n `422`
- 24h: commodity avg `-0.3995` n `12`; crypto_alt avg `-1.0375` n `228`; crypto_major avg `-1.2545` n `8`; equity avg `-0.8142` n `69`; fx avg `0.0111` n `6`; index avg `-0.935` n `23`; metal avg `-0.094` n `18`; unknown avg `1.5225` n `406`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
