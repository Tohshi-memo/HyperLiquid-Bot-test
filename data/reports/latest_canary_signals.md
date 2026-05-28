# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T23:22:16.617683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `12`; crypto_alt avg `-0.0101` n `228`; crypto_major avg `-0.0675` n `8`; equity avg `0.1107` n `69`; fx avg `0.0002` n `6`; index avg `0.021` n `23`; metal avg `0.0208` n `18`; unknown avg `0.038` n `417`
- 1h: commodity avg `-0.0505` n `12`; crypto_alt avg `-0.1264` n `228`; crypto_major avg `-0.0505` n `8`; equity avg `0.1039` n `69`; fx avg `0.0029` n `6`; index avg `-0.0188` n `23`; metal avg `0.0543` n `18`; unknown avg `-0.3251` n `417`
- 4h: commodity avg `-0.1227` n `12`; crypto_alt avg `-0.4049` n `228`; crypto_major avg `-0.0899` n `8`; equity avg `0.7265` n `69`; fx avg `0.0053` n `6`; index avg `-0.0682` n `23`; metal avg `0.0177` n `18`; unknown avg `-0.2874` n `417`
- 24h: commodity avg `0.7483` n `12`; crypto_alt avg `-1.8017` n `228`; crypto_major avg `0.2854` n `8`; equity avg `2.3772` n `69`; fx avg `-0.0038` n `6`; index avg `0.8168` n `23`; metal avg `0.6157` n `18`; unknown avg `-0.1215` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1812`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
