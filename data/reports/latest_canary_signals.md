# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T04:37:29.673086+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0222` n `13`; crypto_alt avg `-0.1365` n `239`; crypto_major avg `-0.0329` n `8`; equity avg `-0.0258` n `158`; fx avg `0.0056` n `6`; index avg `-0.0009` n `27`; metal avg `-0.0056` n `20`; unknown avg `-0.3737` n `1260`
- 1h: commodity avg `0.0025` n `13`; crypto_alt avg `-0.1686` n `239`; crypto_major avg `0.0362` n `8`; equity avg `-0.0839` n `158`; fx avg `0.0019` n `6`; index avg `-0.0103` n `27`; metal avg `-0.0004` n `20`; unknown avg `-0.263` n `1244`
- 4h: commodity avg `0.1108` n `13`; crypto_alt avg `-0.5974` n `239`; crypto_major avg `-0.0522` n `8`; equity avg `-0.0963` n `158`; fx avg `0.0222` n `6`; index avg `-0.0188` n `27`; metal avg `-0.0196` n `20`; unknown avg `-0.3624` n `1240`
- 24h: commodity avg `0.1516` n `13`; crypto_alt avg `-1.8166` n `239`; crypto_major avg `-0.5268` n `8`; equity avg `-0.2227` n `158`; fx avg `0.0199` n `6`; index avg `0.0252` n `27`; metal avg `-0.0612` n `20`; unknown avg `162.7897` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
