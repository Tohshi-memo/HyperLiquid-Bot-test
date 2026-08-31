# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T07:22:25.746482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0707` n `12`; crypto_alt avg `0.2162` n `232`; crypto_major avg `0.1135` n `8`; equity avg `0.0157` n `128`; fx avg `0.006` n `6`; index avg `0.0065` n `26`; metal avg `0.0297` n `20`; unknown avg `0.0671` n `793`
- 1h: commodity avg `-0.2158` n `12`; crypto_alt avg `0.2785` n `232`; crypto_major avg `0.1748` n `8`; equity avg `0.0299` n `128`; fx avg `0.0161` n `6`; index avg `0.0205` n `26`; metal avg `0.0686` n `20`; unknown avg `0.0145` n `791`
- 4h: commodity avg `-0.1` n `12`; crypto_alt avg `1.0335` n `231`; crypto_major avg `0.7399` n `8`; equity avg `0.9812` n `128`; fx avg `-0.0597` n `6`; index avg `0.1763` n `26`; metal avg `0.1316` n `20`; unknown avg `0.3351` n `773`
- 24h: commodity avg `0.2423` n `12`; crypto_alt avg `0.2664` n `231`; crypto_major avg `-1.3817` n `8`; equity avg `-0.165` n `128`; fx avg `-0.1047` n `6`; index avg `-0.0481` n `26`; metal avg `-0.2012` n `20`; unknown avg `-0.436` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
