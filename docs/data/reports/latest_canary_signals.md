# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T02:52:22.688217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0538` n `12`; crypto_alt avg `0.0343` n `228`; crypto_major avg `0.1513` n `8`; equity avg `-0.0109` n `69`; fx avg `0.0147` n `6`; index avg `-0.003` n `23`; metal avg `-0.0014` n `18`; unknown avg `-0.1015` n `421`
- 1h: commodity avg `0.0001` n `12`; crypto_alt avg `-0.0533` n `228`; crypto_major avg `0.0827` n `8`; equity avg `0.0274` n `69`; fx avg `0.0138` n `6`; index avg `-0.0525` n `23`; metal avg `-0.0517` n `18`; unknown avg `-0.3491` n `419`
- 4h: commodity avg `0.0743` n `12`; crypto_alt avg `0.5579` n `228`; crypto_major avg `0.7767` n `8`; equity avg `0.2116` n `69`; fx avg `0.0074` n `6`; index avg `-0.0848` n `23`; metal avg `-0.0544` n `18`; unknown avg `-0.1091` n `419`
- 24h: commodity avg `-0.0138` n `12`; crypto_alt avg `-0.2207` n `228`; crypto_major avg `2.0768` n `8`; equity avg `0.9118` n `69`; fx avg `0.0437` n `6`; index avg `0.0778` n `23`; metal avg `-0.1131` n `18`; unknown avg `1.3462` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
