# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T08:37:37.500827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.0347` n `239`; crypto_major avg `-0.1442` n `8`; equity avg `-0.022` n `168`; fx avg `0.0` n `6`; index avg `-0.0054` n `27`; metal avg `0.0076` n `20`; unknown avg `4.5812` n `1269`
- 1h: commodity avg `-0.0105` n `13`; crypto_alt avg `-0.2598` n `239`; crypto_major avg `-0.2428` n `8`; equity avg `-0.1016` n `168`; fx avg `0.0007` n `6`; index avg `-0.0085` n `27`; metal avg `-0.0079` n `20`; unknown avg `10.7242` n `1245`
- 4h: commodity avg `-0.0095` n `13`; crypto_alt avg `-1.1218` n `239`; crypto_major avg `-0.7843` n `8`; equity avg `-0.2896` n `168`; fx avg `-0.0108` n `6`; index avg `-0.042` n `27`; metal avg `-0.0083` n `20`; unknown avg `40.9398` n `1205`
- 24h: commodity avg `-0.6822` n `13`; crypto_alt avg `-3.1266` n `239`; crypto_major avg `-2.843` n `8`; equity avg `-0.3224` n `168`; fx avg `-0.0801` n `6`; index avg `0.0109` n `27`; metal avg `-0.2544` n `20`; unknown avg `209.3027` n `1013`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
