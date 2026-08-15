# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T01:22:26.708633+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.046` n `12`; crypto_alt avg `-0.0257` n `230`; crypto_major avg `0.0712` n `8`; equity avg `0.0156` n `114`; fx avg `-0.0075` n `6`; index avg `-0.0014` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.0127` n `791`
- 1h: commodity avg `-0.1109` n `12`; crypto_alt avg `-0.153` n `230`; crypto_major avg `0.0243` n `8`; equity avg `0.0304` n `114`; fx avg `-0.0056` n `6`; index avg `-0.0022` n `25`; metal avg `0.0025` n `20`; unknown avg `0.0773` n `791`
- 4h: commodity avg `0.0007` n `12`; crypto_alt avg `0.3019` n `230`; crypto_major avg `0.3438` n `8`; equity avg `0.0326` n `114`; fx avg `-0.0258` n `6`; index avg `-0.0079` n `25`; metal avg `0.0541` n `20`; unknown avg `2.2506` n `791`
- 24h: commodity avg `0.1234` n `12`; crypto_alt avg `0.0107` n `230`; crypto_major avg `-0.7228` n `8`; equity avg `-0.2198` n `114`; fx avg `0.0739` n `6`; index avg `-0.0359` n `25`; metal avg `0.471` n `20`; unknown avg `-0.3496` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1932`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1628`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1555`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1547`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.142`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
