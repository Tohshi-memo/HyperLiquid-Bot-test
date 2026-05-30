# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T23:37:21.632939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0055` n `12`; crypto_alt avg `-0.147` n `228`; crypto_major avg `-0.0226` n `8`; equity avg `-0.0542` n `69`; fx avg `0.0` n `6`; index avg `0.0163` n `23`; metal avg `0.0024` n `18`; unknown avg `0.0116` n `421`
- 1h: commodity avg `-0.0613` n `12`; crypto_alt avg `-0.1455` n `228`; crypto_major avg `0.1241` n `8`; equity avg `0.1302` n `69`; fx avg `-0.0163` n `6`; index avg `0.0525` n `23`; metal avg `-0.0095` n `18`; unknown avg `-0.2086` n `421`
- 4h: commodity avg `0.0639` n `12`; crypto_alt avg `-0.8169` n `228`; crypto_major avg `-0.3769` n `8`; equity avg `0.1952` n `69`; fx avg `-0.0172` n `6`; index avg `0.0105` n `23`; metal avg `-0.0138` n `18`; unknown avg `0.4273` n `421`
- 24h: commodity avg `-0.2449` n `12`; crypto_alt avg `0.8922` n `228`; crypto_major avg `2.703` n `8`; equity avg `1.0547` n `69`; fx avg `0.0159` n `6`; index avg `0.0174` n `23`; metal avg `0.0233` n `18`; unknown avg `1.2147` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
