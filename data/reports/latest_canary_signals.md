# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T12:07:22.047209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.79` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1402` n `12`; crypto_alt avg `-0.2428` n `228`; crypto_major avg `-0.1243` n `8`; equity avg `-0.1069` n `69`; fx avg `-0.007` n `6`; index avg `-0.0457` n `23`; metal avg `-0.1172` n `18`; unknown avg `-0.1568` n `422`
- 1h: commodity avg `-0.0427` n `12`; crypto_alt avg `-0.2344` n `228`; crypto_major avg `-0.1025` n `8`; equity avg `0.2029` n `69`; fx avg `-0.0001` n `6`; index avg `0.0818` n `23`; metal avg `-0.0184` n `18`; unknown avg `-0.2347` n `422`
- 4h: commodity avg `-0.0843` n `12`; crypto_alt avg `-0.0367` n `228`; crypto_major avg `-0.2448` n `8`; equity avg `-0.0316` n `69`; fx avg `-0.0145` n `6`; index avg `0.0878` n `23`; metal avg `-0.489` n `18`; unknown avg `-0.3839` n `422`
- 24h: commodity avg `-0.7458` n `12`; crypto_alt avg `0.2239` n `228`; crypto_major avg `-1.6667` n `8`; equity avg `0.8074` n `69`; fx avg `0.1432` n `6`; index avg `0.1063` n `23`; metal avg `0.601` n `18`; unknown avg `-0.0248` n `412`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.165`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
