# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T23:37:19.100127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0479` n `12`; crypto_alt avg `0.1473` n `228`; crypto_major avg `0.1436` n `8`; equity avg `0.0427` n `69`; fx avg `0.0092` n `6`; index avg `-0.0029` n `23`; metal avg `0.0095` n `18`; unknown avg `0.0703` n `417`
- 1h: commodity avg `-0.1438` n `12`; crypto_alt avg `0.3006` n `228`; crypto_major avg `0.256` n `8`; equity avg `0.2405` n `69`; fx avg `0.0102` n `6`; index avg `0.0519` n `23`; metal avg `0.0497` n `18`; unknown avg `-0.0591` n `417`
- 4h: commodity avg `0.077` n `12`; crypto_alt avg `-0.1476` n `228`; crypto_major avg `0.1057` n `8`; equity avg `0.5616` n `69`; fx avg `0.0149` n `6`; index avg `-0.1428` n `23`; metal avg `-0.0164` n `18`; unknown avg `-0.1865` n `417`
- 24h: commodity avg `0.6951` n `12`; crypto_alt avg `-1.5204` n `228`; crypto_major avg `0.6678` n `8`; equity avg `2.5744` n `69`; fx avg `0.0099` n `6`; index avg `0.8733` n `23`; metal avg `0.6118` n `18`; unknown avg `0.1385` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1557`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
