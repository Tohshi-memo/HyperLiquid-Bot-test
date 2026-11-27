# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T14:22:36.848493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0065` n `13`; crypto_alt avg `-0.1907` n `239`; crypto_major avg `-0.152` n `8`; equity avg `-0.0231` n `168`; fx avg `-0.0061` n `6`; index avg `-0.0106` n `27`; metal avg `0.0347` n `20`; unknown avg `159.8393` n `1262`
- 1h: commodity avg `-0.0046` n `13`; crypto_alt avg `-0.1044` n `239`; crypto_major avg `-0.1202` n `8`; equity avg `-0.1844` n `168`; fx avg `0.0042` n `6`; index avg `-0.0583` n `27`; metal avg `0.0098` n `20`; unknown avg `5.3602` n `1258`
- 4h: commodity avg `-0.3904` n `13`; crypto_alt avg `-0.0154` n `239`; crypto_major avg `-0.2436` n `8`; equity avg `-0.5238` n `168`; fx avg `-0.0133` n `6`; index avg `-0.0414` n `27`; metal avg `-0.4011` n `20`; unknown avg `5.3651` n `1251`
- 24h: commodity avg `-0.3125` n `13`; crypto_alt avg `1.6088` n `239`; crypto_major avg `2.3711` n `8`; equity avg `3.2925` n `168`; fx avg `-0.1254` n `6`; index avg `0.2667` n `27`; metal avg `0.829` n `20`; unknown avg `276.5947` n `1031`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
