# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T16:07:18.671874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.8461` n `12`; crypto_alt avg `0.1328` n `228`; crypto_major avg `0.0456` n `8`; equity avg `-0.0576` n `69`; fx avg `-0.0107` n `6`; index avg `-0.0949` n `23`; metal avg `0.0126` n `18`; unknown avg `-0.0144` n `421`
- 1h: commodity avg `-0.8531` n `12`; crypto_alt avg `0.0606` n `228`; crypto_major avg `0.0684` n `8`; equity avg `-0.139` n `69`; fx avg `-0.0099` n `6`; index avg `-0.1932` n `23`; metal avg `0.0497` n `18`; unknown avg `0.1186` n `421`
- 4h: commodity avg `-0.7616` n `12`; crypto_alt avg `0.2523` n `228`; crypto_major avg `0.6318` n `8`; equity avg `0.1689` n `69`; fx avg `0.0144` n `6`; index avg `-0.0302` n `23`; metal avg `0.0195` n `18`; unknown avg `0.0004` n `421`
- 24h: commodity avg `-0.7805` n `12`; crypto_alt avg `0.6268` n `228`; crypto_major avg `1.6412` n `8`; equity avg `0.8174` n `69`; fx avg `-0.0025` n `6`; index avg `0.073` n `23`; metal avg `-0.1781` n `18`; unknown avg `0.0661` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
