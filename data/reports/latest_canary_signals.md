# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T00:07:15.946143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1421` n `12`; crypto_alt avg `0.0412` n `228`; crypto_major avg `0.0241` n `8`; equity avg `0.0097` n `65`; fx avg `0.0015` n `5`; index avg `0.0915` n `23`; metal avg `0.0042` n `18`; unknown avg `-0.1135` n `375`
- 1h: commodity avg `-0.1568` n `12`; crypto_alt avg `0.0195` n `228`; crypto_major avg `-0.0302` n `8`; equity avg `0.0252` n `65`; fx avg `0.0006` n `5`; index avg `0.1077` n `23`; metal avg `-0.0601` n `18`; unknown avg `-0.3086` n `375`
- 4h: commodity avg `-0.2817` n `12`; crypto_alt avg `0.6171` n `228`; crypto_major avg `0.1117` n `8`; equity avg `0.275` n `65`; fx avg `-0.022` n `5`; index avg `0.169` n `23`; metal avg `-0.3481` n `18`; unknown avg `-0.4192` n `375`
- 24h: commodity avg `-0.7428` n `12`; crypto_alt avg `3.253` n `228`; crypto_major avg `1.4213` n `8`; equity avg `3.902` n `65`; fx avg `0.1692` n `5`; index avg `1.5664` n `23`; metal avg `0.4341` n `18`; unknown avg `0.7952` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
