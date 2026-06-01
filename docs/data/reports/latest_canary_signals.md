# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T13:37:28.061455+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1652` n `12`; crypto_alt avg `0.1077` n `228`; crypto_major avg `-0.1846` n `8`; equity avg `-0.0732` n `69`; fx avg `-0.0283` n `6`; index avg `-0.1183` n `23`; metal avg `-0.0167` n `18`; unknown avg `-0.101` n `422`
- 1h: commodity avg `0.7242` n `12`; crypto_alt avg `-0.2376` n `228`; crypto_major avg `-0.6003` n `8`; equity avg `-0.4687` n `69`; fx avg `-0.0543` n `6`; index avg `-0.3309` n `23`; metal avg `-0.708` n `18`; unknown avg `0.8637` n `422`
- 4h: commodity avg `-0.2286` n `12`; crypto_alt avg `-0.1505` n `228`; crypto_major avg `-0.7312` n `8`; equity avg `-0.7942` n `69`; fx avg `-0.0383` n `6`; index avg `-0.383` n `23`; metal avg `-0.6607` n `18`; unknown avg `2.3083` n `416`
- 24h: commodity avg `0.8436` n `12`; crypto_alt avg `-1.0355` n `228`; crypto_major avg `-1.5683` n `8`; equity avg `-1.0541` n `69`; fx avg `-0.0455` n `6`; index avg `0.1055` n `23`; metal avg `-0.5448` n `18`; unknown avg `4.1862` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2879`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2139`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1502`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
