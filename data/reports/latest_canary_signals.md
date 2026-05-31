# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T08:07:16.021227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0305` n `12`; crypto_alt avg `0.274` n `228`; crypto_major avg `0.1644` n `8`; equity avg `0.0149` n `69`; fx avg `-0.0049` n `6`; index avg `0.0394` n `23`; metal avg `0.0039` n `18`; unknown avg `0.0841` n `421`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `-0.1725` n `228`; crypto_major avg `-0.195` n `8`; equity avg `0.2416` n `69`; fx avg `-0.0219` n `6`; index avg `0.0186` n `23`; metal avg `-0.0033` n `18`; unknown avg `0.6315` n `421`
- 4h: commodity avg `0.2259` n `12`; crypto_alt avg `-0.3774` n `228`; crypto_major avg `-0.3623` n `8`; equity avg `0.4241` n `69`; fx avg `-0.0056` n `6`; index avg `0.0177` n `23`; metal avg `0.0054` n `18`; unknown avg `0.1283` n `401`
- 24h: commodity avg `0.241` n `12`; crypto_alt avg `0.2237` n `228`; crypto_major avg `1.6691` n `8`; equity avg `1.254` n `69`; fx avg `0.0371` n `6`; index avg `-0.0246` n `23`; metal avg `-0.016` n `18`; unknown avg `1.6289` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
