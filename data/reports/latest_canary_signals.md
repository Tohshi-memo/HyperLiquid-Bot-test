# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T12:52:33.960633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0118` n `12`; crypto_alt avg `0.0416` n `230`; crypto_major avg `-0.1301` n `8`; equity avg `-0.0327` n `114`; fx avg `0.0164` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0342` n `20`; unknown avg `-0.0671` n `786`
- 1h: commodity avg `0.0178` n `12`; crypto_alt avg `-0.1164` n `230`; crypto_major avg `-0.2165` n `8`; equity avg `-0.0882` n `114`; fx avg `-0.0254` n `6`; index avg `-0.0094` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.0355` n `786`
- 4h: commodity avg `-0.1939` n `12`; crypto_alt avg `-0.271` n `230`; crypto_major avg `-0.4685` n `8`; equity avg `0.2615` n `114`; fx avg `0.0058` n `6`; index avg `0.0383` n `25`; metal avg `0.1235` n `20`; unknown avg `3.2495` n `786`
- 24h: commodity avg `-0.0666` n `12`; crypto_alt avg `-0.8073` n `230`; crypto_major avg `-1.001` n `8`; equity avg `1.8456` n `114`; fx avg `-0.0416` n `6`; index avg `0.3324` n `25`; metal avg `-0.131` n `20`; unknown avg `0.887` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2268`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
