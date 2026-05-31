# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T08:52:21.529752+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.027` n `12`; crypto_alt avg `-0.1666` n `228`; crypto_major avg `-0.0455` n `8`; equity avg `0.0196` n `69`; fx avg `-0.0056` n `6`; index avg `-0.0278` n `23`; metal avg `0.0054` n `18`; unknown avg `0.0277` n `421`
- 1h: commodity avg `0.0124` n `12`; crypto_alt avg `0.0955` n `228`; crypto_major avg `0.0752` n `8`; equity avg `-0.0408` n `69`; fx avg `0.0005` n `6`; index avg `-0.0673` n `23`; metal avg `-0.0017` n `18`; unknown avg `0.1045` n `421`
- 4h: commodity avg `0.1817` n `12`; crypto_alt avg `-0.8098` n `228`; crypto_major avg `-0.6061` n `8`; equity avg `0.3544` n `69`; fx avg `-0.0039` n `6`; index avg `-0.0712` n `23`; metal avg `0.0268` n `18`; unknown avg `0.7964` n `401`
- 24h: commodity avg `0.2639` n `12`; crypto_alt avg `0.0847` n `228`; crypto_major avg `1.6016` n `8`; equity avg `1.1832` n `69`; fx avg `0.045` n `6`; index avg `-0.1049` n `23`; metal avg `-0.0196` n `18`; unknown avg `1.7047` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
