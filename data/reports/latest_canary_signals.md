# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T21:22:26.561998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0375` n `13`; crypto_alt avg `-0.0358` n `239`; crypto_major avg `0.0031` n `8`; equity avg `-0.0651` n `158`; fx avg `-0.0061` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0063` n `20`; unknown avg `0.8113` n `1262`
- 1h: commodity avg `0.0033` n `13`; crypto_alt avg `-0.7173` n `239`; crypto_major avg `-0.394` n `8`; equity avg `-0.1878` n `158`; fx avg `-0.0114` n `6`; index avg `-0.0238` n `27`; metal avg `-0.0087` n `20`; unknown avg `0.1891` n `1228`
- 4h: commodity avg `0.0184` n `13`; crypto_alt avg `-0.8866` n `239`; crypto_major avg `-0.4592` n `8`; equity avg `-0.1344` n `158`; fx avg `-0.0097` n `6`; index avg `-0.0242` n `27`; metal avg `-0.0136` n `20`; unknown avg `-0.226` n `1194`
- 24h: commodity avg `0.1037` n `13`; crypto_alt avg `-2.4105` n `239`; crypto_major avg `-1.0806` n `8`; equity avg `-0.2385` n `158`; fx avg `-0.0213` n `6`; index avg `0.0178` n `27`; metal avg `-0.0021` n `20`; unknown avg `-0.3744` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
