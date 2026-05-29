# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T04:37:18.569530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0975` n `12`; crypto_alt avg `0.2699` n `228`; crypto_major avg `0.2572` n `8`; equity avg `0.1266` n `69`; fx avg `0.0012` n `6`; index avg `0.0439` n `23`; metal avg `0.0863` n `18`; unknown avg `-0.1211` n `417`
- 1h: commodity avg `0.0263` n `12`; crypto_alt avg `0.0563` n `228`; crypto_major avg `0.0247` n `8`; equity avg `0.2289` n `69`; fx avg `-0.0107` n `6`; index avg `0.1535` n `23`; metal avg `0.2569` n `18`; unknown avg `-0.6445` n `417`
- 4h: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.6976` n `228`; crypto_major avg `-0.6046` n `8`; equity avg `0.2086` n `69`; fx avg `-0.0086` n `6`; index avg `0.1017` n `23`; metal avg `0.1714` n `18`; unknown avg `-0.9449` n `417`
- 24h: commodity avg `-0.3091` n `12`; crypto_alt avg `0.638` n `228`; crypto_major avg `1.6087` n `8`; equity avg `4.6753` n `69`; fx avg `0.1414` n `6`; index avg `1.7669` n `23`; metal avg `2.7123` n `18`; unknown avg `0.5612` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1292`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
