# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T11:37:35.568148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0745` n `13`; crypto_alt avg `-0.5551` n `239`; crypto_major avg `-0.6577` n `8`; equity avg `-0.2327` n `162`; fx avg `0.0123` n `6`; index avg `-0.0093` n `27`; metal avg `-0.0374` n `20`; unknown avg `0.0454` n `1261`
- 1h: commodity avg `0.0167` n `13`; crypto_alt avg `-0.7421` n `239`; crypto_major avg `-1.0256` n `8`; equity avg `-0.6245` n `162`; fx avg `0.0059` n `6`; index avg `-0.041` n `27`; metal avg `-0.0855` n `20`; unknown avg `0.2464` n `1255`
- 4h: commodity avg `-0.0952` n `13`; crypto_alt avg `-0.6169` n `239`; crypto_major avg `-0.7712` n `8`; equity avg `-0.0297` n `162`; fx avg `0.0092` n `6`; index avg `0.0296` n `27`; metal avg `-0.1708` n `20`; unknown avg `-0.0685` n `1233`
- 24h: commodity avg `-0.0422` n `13`; crypto_alt avg `-2.2255` n `239`; crypto_major avg `-1.6652` n `8`; equity avg `-1.3849` n `162`; fx avg `-0.0772` n `6`; index avg `-0.0918` n `27`; metal avg `-0.9221` n `20`; unknown avg `-0.0696` n `1140`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
