# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T07:22:17.009815+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `0.0066` n `228`; crypto_major avg `0.1233` n `8`; equity avg `0.0173` n `69`; fx avg `0.0006` n `6`; index avg `0.0385` n `23`; metal avg `-0.0063` n `18`; unknown avg `0.8368` n `421`
- 1h: commodity avg `0.0448` n `12`; crypto_alt avg `-0.251` n `228`; crypto_major avg `0.0713` n `8`; equity avg `0.056` n `69`; fx avg `0.0005` n `6`; index avg `0.0436` n `23`; metal avg `0.0032` n `18`; unknown avg `-0.1117` n `421`
- 4h: commodity avg `-0.08` n `12`; crypto_alt avg `-0.543` n `228`; crypto_major avg `0.0768` n `8`; equity avg `0.1238` n `69`; fx avg `0.0043` n `6`; index avg `0.1354` n `23`; metal avg `-0.0115` n `18`; unknown avg `0.9798` n `401`
- 24h: commodity avg `-0.4172` n `12`; crypto_alt avg `0.8429` n `228`; crypto_major avg `1.6554` n `8`; equity avg `0.8547` n `69`; fx avg `0.0456` n `6`; index avg `0.1542` n `23`; metal avg `0.0253` n `18`; unknown avg `1.245` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1146`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
