# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T14:37:28.359287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0125` n `12`; crypto_alt avg `0.0429` n `230`; crypto_major avg `0.0514` n `8`; equity avg `0.0689` n `114`; fx avg `-0.0133` n `6`; index avg `0.0222` n `25`; metal avg `0.0314` n `20`; unknown avg `0.0072` n `792`
- 1h: commodity avg `0.0179` n `12`; crypto_alt avg `-0.1479` n `230`; crypto_major avg `-0.1423` n `8`; equity avg `0.2538` n `114`; fx avg `-0.0228` n `6`; index avg `0.0485` n `25`; metal avg `0.2028` n `20`; unknown avg `0.0309` n `792`
- 4h: commodity avg `0.0773` n `12`; crypto_alt avg `-0.0252` n `230`; crypto_major avg `-0.1406` n `8`; equity avg `-0.12` n `114`; fx avg `-0.0023` n `6`; index avg `0.0167` n `25`; metal avg `0.0799` n `20`; unknown avg `1.1911` n `792`
- 24h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.1428` n `230`; crypto_major avg `0.6525` n `8`; equity avg `1.2119` n `114`; fx avg `0.0007` n `6`; index avg `0.1662` n `25`; metal avg `0.2712` n `20`; unknown avg `0.121` n `775`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
