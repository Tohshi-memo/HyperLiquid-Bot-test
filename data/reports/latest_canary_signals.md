# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T09:52:19.958255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `-0.0364` n `228`; crypto_major avg `0.0235` n `8`; equity avg `-0.0189` n `69`; fx avg `-0.0063` n `6`; index avg `-0.0069` n `23`; metal avg `-0.017` n `18`; unknown avg `-0.0245` n `421`
- 1h: commodity avg `-0.0253` n `12`; crypto_alt avg `0.1072` n `228`; crypto_major avg `0.12` n `8`; equity avg `0.022` n `69`; fx avg `0.0233` n `6`; index avg `-0.051` n `23`; metal avg `0.0372` n `18`; unknown avg `0.1989` n `421`
- 4h: commodity avg `-0.0425` n `12`; crypto_alt avg `-0.1707` n `228`; crypto_major avg `0.1658` n `8`; equity avg `0.0708` n `69`; fx avg `0.0197` n `6`; index avg `-0.0031` n `23`; metal avg `0.0437` n `18`; unknown avg `-0.0444` n `401`
- 24h: commodity avg `-0.2378` n `12`; crypto_alt avg `1.1295` n `228`; crypto_major avg `1.6871` n `8`; equity avg `1.0342` n `69`; fx avg `0.1081` n `6`; index avg `0.0452` n `23`; metal avg `-0.1289` n `18`; unknown avg `0.3889` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1929`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
