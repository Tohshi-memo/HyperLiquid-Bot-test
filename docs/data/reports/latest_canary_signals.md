# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T06:22:20.126008+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1444` n `12`; crypto_alt avg `-0.2514` n `228`; crypto_major avg `0.0076` n `8`; equity avg `-0.1304` n `69`; fx avg `-0.0078` n `6`; index avg `0.0235` n `23`; metal avg `-0.2165` n `18`; unknown avg `0.7101` n `422`
- 1h: commodity avg `0.2714` n `12`; crypto_alt avg `-0.8861` n `228`; crypto_major avg `-0.4612` n `8`; equity avg `-0.1029` n `69`; fx avg `-0.0656` n `6`; index avg `-0.0721` n `23`; metal avg `-0.2785` n `18`; unknown avg `0.7289` n `412`
- 4h: commodity avg `0.2256` n `12`; crypto_alt avg `-0.6852` n `228`; crypto_major avg `-0.3554` n `8`; equity avg `0.0049` n `69`; fx avg `-0.0918` n `6`; index avg `0.3575` n `23`; metal avg `-0.3374` n `18`; unknown avg `0.0253` n `412`
- 24h: commodity avg `1.1486` n `12`; crypto_alt avg `-0.2853` n `228`; crypto_major avg `-0.938` n `8`; equity avg `0.3124` n `69`; fx avg `-0.049` n `6`; index avg `0.5059` n `23`; metal avg `0.1306` n `18`; unknown avg `2.8492` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2871`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2268`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
