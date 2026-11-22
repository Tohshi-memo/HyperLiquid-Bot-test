# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T17:22:28.575096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `13`; crypto_alt avg `-0.0504` n `239`; crypto_major avg `-0.1034` n `8`; equity avg `0.0079` n `166`; fx avg `0.0013` n `6`; index avg `0.0009` n `27`; metal avg `0.0079` n `20`; unknown avg `-0.2796` n `1261`
- 1h: commodity avg `-0.0117` n `13`; crypto_alt avg `-0.2812` n `239`; crypto_major avg `-0.3832` n `8`; equity avg `0.0654` n `166`; fx avg `0.0015` n `6`; index avg `0.0101` n `27`; metal avg `0.006` n `20`; unknown avg `159.5263` n `1251`
- 4h: commodity avg `-0.0297` n `13`; crypto_alt avg `0.1145` n `239`; crypto_major avg `0.3261` n `8`; equity avg `0.1005` n `166`; fx avg `0.0146` n `6`; index avg `0.045` n `27`; metal avg `0.0675` n `20`; unknown avg `162.12` n `1231`
- 24h: commodity avg `-0.0406` n `13`; crypto_alt avg `0.7523` n `239`; crypto_major avg `0.8069` n `8`; equity avg `0.9945` n `166`; fx avg `0.003` n `6`; index avg `0.1635` n `27`; metal avg `0.0619` n `20`; unknown avg `188.0017` n `1064`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
