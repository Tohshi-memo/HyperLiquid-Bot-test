# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T11:37:29.394168+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.0362` n `230`; crypto_major avg `-0.0207` n `8`; equity avg `-0.0026` n `114`; fx avg `-0.0131` n `6`; index avg `-0.0002` n `25`; metal avg `0.0063` n `20`; unknown avg `-0.0411` n `791`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `0.0668` n `230`; crypto_major avg `0.0258` n `8`; equity avg `-0.0408` n `114`; fx avg `-0.0076` n `6`; index avg `0.0023` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0831` n `791`
- 4h: commodity avg `0.0048` n `12`; crypto_alt avg `0.126` n `230`; crypto_major avg `-0.0473` n `8`; equity avg `-0.0412` n `114`; fx avg `-0.0132` n `6`; index avg `-0.012` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0425` n `791`
- 24h: commodity avg `0.0208` n `12`; crypto_alt avg `0.124` n `230`; crypto_major avg `0.1447` n `8`; equity avg `0.3345` n `114`; fx avg `-0.0111` n `6`; index avg `0.0504` n `25`; metal avg `0.0245` n `20`; unknown avg `0.0728` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2125`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
