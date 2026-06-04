# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T13:07:29.594353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0739` n `12`; crypto_alt avg `-0.3749` n `228`; crypto_major avg `-0.4074` n `8`; equity avg `-0.1924` n `73`; fx avg `0.0048` n `6`; index avg `-0.0297` n `23`; metal avg `0.1566` n `18`; unknown avg `-0.1015` n `425`
- 1h: commodity avg `0.2044` n `12`; crypto_alt avg `1.9475` n `228`; crypto_major avg `1.5416` n `8`; equity avg `0.4759` n `73`; fx avg `0.0121` n `6`; index avg `0.1458` n `23`; metal avg `0.3839` n `18`; unknown avg `1.4434` n `422`
- 4h: commodity avg `-0.222` n `12`; crypto_alt avg `0.6318` n `228`; crypto_major avg `0.6325` n `8`; equity avg `0.3098` n `73`; fx avg `0.0444` n `6`; index avg `-0.0511` n `23`; metal avg `1.0487` n `18`; unknown avg `0.1315` n `422`
- 24h: commodity avg `-0.5632` n `12`; crypto_alt avg `-6.4175` n `228`; crypto_major avg `-5.1074` n `8`; equity avg `-3.9747` n `73`; fx avg `0.1242` n `6`; index avg `-1.3869` n `23`; metal avg `0.0243` n `18`; unknown avg `-0.4296` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
