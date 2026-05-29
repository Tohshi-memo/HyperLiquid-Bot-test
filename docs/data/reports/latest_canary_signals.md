# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T11:37:19.099951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1674` n `12`; crypto_alt avg `-0.3935` n `228`; crypto_major avg `-0.3134` n `8`; equity avg `-0.1398` n `69`; fx avg `0.0045` n `6`; index avg `-0.0489` n `23`; metal avg `-0.1524` n `18`; unknown avg `-0.0841` n `417`
- 1h: commodity avg `0.1644` n `12`; crypto_alt avg `-0.2897` n `228`; crypto_major avg `-0.409` n `8`; equity avg `-0.253` n `69`; fx avg `-0.0059` n `6`; index avg `0.1176` n `23`; metal avg `-0.1983` n `18`; unknown avg `0.8196` n `417`
- 4h: commodity avg `-0.32` n `12`; crypto_alt avg `-0.0639` n `228`; crypto_major avg `0.0202` n `8`; equity avg `-0.2722` n `69`; fx avg `-0.0351` n `6`; index avg `0.1724` n `23`; metal avg `0.0489` n `18`; unknown avg `-0.0744` n `417`
- 24h: commodity avg `-0.1339` n `12`; crypto_alt avg `1.6767` n `228`; crypto_major avg `2.0256` n `8`; equity avg `3.4149` n `69`; fx avg `0.14` n `6`; index avg `1.566` n `23`; metal avg `2.166` n `18`; unknown avg `2.0165` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
