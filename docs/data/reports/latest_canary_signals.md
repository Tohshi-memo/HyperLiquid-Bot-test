# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T10:22:28.714723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `13`; crypto_alt avg `0.1779` n `239`; crypto_major avg `0.1486` n `8`; equity avg `0.0548` n `162`; fx avg `-0.0044` n `6`; index avg `0.0048` n `27`; metal avg `-0.0454` n `20`; unknown avg `-0.1429` n `1232`
- 1h: commodity avg `-0.1186` n `13`; crypto_alt avg `0.2976` n `239`; crypto_major avg `0.5775` n `8`; equity avg `0.2524` n `162`; fx avg `-0.0282` n `6`; index avg `0.0257` n `27`; metal avg `0.0071` n `20`; unknown avg `0.0126` n `1228`
- 4h: commodity avg `-0.041` n `13`; crypto_alt avg `0.7442` n `239`; crypto_major avg `0.9601` n `8`; equity avg `0.4071` n `162`; fx avg `-0.0198` n `6`; index avg `0.0421` n `27`; metal avg `-0.0761` n `20`; unknown avg `0.5657` n `1168`
- 24h: commodity avg `0.6545` n `13`; crypto_alt avg `-1.0712` n `239`; crypto_major avg `-2.9447` n `8`; equity avg `-1.3016` n `162`; fx avg `-0.0389` n `6`; index avg `0.0044` n `27`; metal avg `-0.4415` n `20`; unknown avg `81.9009` n `1089`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
