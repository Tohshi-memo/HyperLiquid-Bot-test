# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T02:37:30.485922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0165` n `12`; crypto_alt avg `-0.0438` n `230`; crypto_major avg `-0.0429` n `8`; equity avg `-0.0187` n `114`; fx avg `0.1184` n `6`; index avg `-0.0006` n `25`; metal avg `-0.0014` n `20`; unknown avg `-0.0616` n `791`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `0.0834` n `230`; crypto_major avg `0.0915` n `8`; equity avg `0.008` n `114`; fx avg `0.1195` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0097` n `20`; unknown avg `0.1086` n `791`
- 4h: commodity avg `-0.0147` n `12`; crypto_alt avg `0.285` n `230`; crypto_major avg `0.4545` n `8`; equity avg `-0.0059` n `114`; fx avg `0.0969` n `6`; index avg `-0.0084` n `25`; metal avg `0.038` n `20`; unknown avg `0.2475` n `791`
- 24h: commodity avg `0.1629` n `12`; crypto_alt avg `0.0989` n `230`; crypto_major avg `-0.5177` n `8`; equity avg `-0.2438` n `114`; fx avg `0.2314` n `6`; index avg `-0.0531` n `25`; metal avg `0.402` n `20`; unknown avg `-0.1676` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2176`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1851`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
