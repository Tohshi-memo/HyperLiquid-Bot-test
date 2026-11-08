# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T01:52:23.442629+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0214` n `13`; crypto_alt avg `-0.1179` n `239`; crypto_major avg `-0.0933` n `8`; equity avg `-0.0318` n `158`; fx avg `0.0111` n `6`; index avg `-0.0086` n `27`; metal avg `-0.0144` n `20`; unknown avg `2.7566` n `1262`
- 1h: commodity avg `0.035` n `13`; crypto_alt avg `-0.4181` n `239`; crypto_major avg `-0.1022` n `8`; equity avg `-0.0821` n `158`; fx avg `0.0169` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0118` n `20`; unknown avg `0.5096` n `1254`
- 4h: commodity avg `-0.0532` n `13`; crypto_alt avg `-0.1151` n `239`; crypto_major avg `0.1309` n `8`; equity avg `0.0554` n `158`; fx avg `0.0209` n `6`; index avg `0.0059` n `27`; metal avg `-0.0076` n `20`; unknown avg `0.3259` n `1226`
- 24h: commodity avg `0.0858` n `13`; crypto_alt avg `-2.0785` n `239`; crypto_major avg `-1.0332` n `8`; equity avg `-0.3284` n `158`; fx avg `0.0167` n `6`; index avg `0.0338` n `27`; metal avg `-0.0549` n `20`; unknown avg `161.4235` n `1085`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
