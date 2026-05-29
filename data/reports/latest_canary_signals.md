# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T07:22:19.366716+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2395` n `12`; crypto_alt avg `0.2145` n `228`; crypto_major avg `0.134` n `8`; equity avg `-0.0902` n `69`; fx avg `-0.0105` n `6`; index avg `-0.0496` n `23`; metal avg `-0.1962` n `18`; unknown avg `0.1457` n `417`
- 1h: commodity avg `0.3266` n `12`; crypto_alt avg `0.2282` n `228`; crypto_major avg `0.1029` n `8`; equity avg `0.0062` n `69`; fx avg `0.0122` n `6`; index avg `-0.1118` n `23`; metal avg `-0.1317` n `18`; unknown avg `0.2417` n `417`
- 4h: commodity avg `0.2501` n `12`; crypto_alt avg `0.8941` n `228`; crypto_major avg `0.6285` n `8`; equity avg `0.4224` n `69`; fx avg `0.0643` n `6`; index avg `0.1132` n `23`; metal avg `0.1285` n `18`; unknown avg `0.2644` n `407`
- 24h: commodity avg `0.2749` n `12`; crypto_alt avg `1.5995` n `228`; crypto_major avg `1.9945` n `8`; equity avg `3.7848` n `69`; fx avg `0.1488` n `6`; index avg `1.2338` n `23`; metal avg `1.6387` n `18`; unknown avg `1.0531` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1497`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
