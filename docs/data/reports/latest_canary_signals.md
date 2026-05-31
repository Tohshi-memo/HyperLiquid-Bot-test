# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T23:37:21.676161+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0865` n `12`; crypto_alt avg `-0.2946` n `228`; crypto_major avg `-0.3333` n `8`; equity avg `-0.0299` n `69`; fx avg `0.0021` n `6`; index avg `0.175` n `23`; metal avg `0.0793` n `18`; unknown avg `-0.1898` n `421`
- 1h: commodity avg `-0.0938` n `12`; crypto_alt avg `-0.3762` n `228`; crypto_major avg `-0.5354` n `8`; equity avg `-0.0601` n `69`; fx avg `0.0012` n `6`; index avg `-0.1168` n `23`; metal avg `0.2908` n `18`; unknown avg `-0.0121` n `421`
- 4h: commodity avg `0.2233` n `12`; crypto_alt avg `1.4731` n `228`; crypto_major avg `0.8194` n `8`; equity avg `-0.0202` n `69`; fx avg `-0.0109` n `6`; index avg `-0.0781` n `23`; metal avg `0.2782` n `18`; unknown avg `1.436` n `421`
- 24h: commodity avg `0.8089` n `12`; crypto_alt avg `0.879` n `228`; crypto_major avg `0.2413` n `8`; equity avg `0.636` n `69`; fx avg `-0.0185` n `6`; index avg `0.2216` n `23`; metal avg `0.1609` n `18`; unknown avg `1.7674` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3389`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2546`, n `668`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
