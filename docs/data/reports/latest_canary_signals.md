# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T08:22:20.214187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `12`; crypto_alt avg `-0.0162` n `228`; crypto_major avg `-0.0632` n `8`; equity avg `0.0298` n `69`; fx avg `-0.0149` n `6`; index avg `0.0066` n `23`; metal avg `0.0119` n `18`; unknown avg `-0.1862` n `421`
- 1h: commodity avg `-0.0525` n `12`; crypto_alt avg `0.034` n `228`; crypto_major avg `-0.0916` n `8`; equity avg `0.0429` n `69`; fx avg `-0.015` n `6`; index avg `-0.0036` n `23`; metal avg `-0.0022` n `18`; unknown avg `-0.2678` n `421`
- 4h: commodity avg `-0.136` n `12`; crypto_alt avg `0.3054` n `228`; crypto_major avg `0.5499` n `8`; equity avg `0.2926` n `69`; fx avg `-0.0107` n `6`; index avg `0.1592` n `23`; metal avg `0.0595` n `18`; unknown avg `-0.2608` n `401`
- 24h: commodity avg `-0.7558` n `12`; crypto_alt avg `1.1045` n `228`; crypto_major avg `1.5123` n `8`; equity avg `1.0103` n `69`; fx avg `0.0628` n `6`; index avg `0.158` n `23`; metal avg `0.1744` n `18`; unknown avg `0.1551` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1916`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
