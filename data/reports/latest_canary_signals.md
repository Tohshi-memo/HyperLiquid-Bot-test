# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T23:00:00.269917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0907` n `12`; crypto_alt avg `-0.049` n `228`; crypto_major avg `0.018` n `8`; equity avg `-0.0059` n `69`; fx avg `-0.0005` n `6`; index avg `0.0351` n `23`; metal avg `-0.0356` n `18`; unknown avg `-0.1394` n `417`
- 1h: commodity avg `-0.0334` n `12`; crypto_alt avg `-0.4907` n `228`; crypto_major avg `-0.2714` n `8`; equity avg `0.0941` n `69`; fx avg `-0.0015` n `6`; index avg `-0.0056` n `23`; metal avg `-0.1294` n `18`; unknown avg `-0.3282` n `417`
- 4h: commodity avg `-0.2125` n `12`; crypto_alt avg `-0.5116` n `228`; crypto_major avg `-0.1362` n `8`; equity avg `0.5001` n `69`; fx avg `-0.0076` n `6`; index avg `-0.1576` n `23`; metal avg `-0.0907` n `18`; unknown avg `-0.2192` n `417`
- 24h: commodity avg `0.7753` n `12`; crypto_alt avg `-2.0574` n `228`; crypto_major avg `0.1903` n `8`; equity avg `2.2458` n `69`; fx avg `-0.0182` n `6`; index avg `0.7927` n `23`; metal avg `0.4645` n `18`; unknown avg `-0.2007` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1804`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
