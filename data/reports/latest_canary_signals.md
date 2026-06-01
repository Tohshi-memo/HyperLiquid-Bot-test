# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T05:07:20.707970+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1044` n `12`; crypto_alt avg `0.0653` n `228`; crypto_major avg `0.0588` n `8`; equity avg `0.0419` n `69`; fx avg `-0.0183` n `6`; index avg `0.0061` n `23`; metal avg `0.1226` n `18`; unknown avg `-0.05` n `422`
- 1h: commodity avg `-0.2013` n `12`; crypto_alt avg `-0.5777` n `228`; crypto_major avg `-0.3243` n `8`; equity avg `0.0468` n `69`; fx avg `0.0037` n `6`; index avg `0.0496` n `23`; metal avg `0.168` n `18`; unknown avg `-0.5271` n `422`
- 4h: commodity avg `-0.1116` n `12`; crypto_alt avg `-0.3504` n `228`; crypto_major avg `-0.4644` n `8`; equity avg `-0.2658` n `69`; fx avg `-0.0037` n `6`; index avg `0.472` n `23`; metal avg `0.2125` n `18`; unknown avg `-0.6364` n `421`
- 24h: commodity avg `0.7883` n `12`; crypto_alt avg `0.2075` n `228`; crypto_major avg `-0.772` n `8`; equity avg `0.5898` n `69`; fx avg `0.0188` n `6`; index avg `0.7912` n `23`; metal avg `0.2706` n `18`; unknown avg `1.3846` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2877`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2245`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
