# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T07:37:32.898365+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0368` n `13`; crypto_alt avg `-0.1246` n `239`; crypto_major avg `-0.1177` n `8`; equity avg `-0.0903` n `158`; fx avg `-0.0195` n `6`; index avg `0.0127` n `27`; metal avg `-0.0109` n `20`; unknown avg `0.0591` n `1263`
- 1h: commodity avg `0.2223` n `13`; crypto_alt avg `-0.2866` n `239`; crypto_major avg `-0.0489` n `8`; equity avg `0.2447` n `158`; fx avg `-0.0403` n `6`; index avg `0.0479` n `27`; metal avg `-0.0341` n `20`; unknown avg `0.6509` n `1255`
- 4h: commodity avg `0.3374` n `13`; crypto_alt avg `-1.0209` n `239`; crypto_major avg `-0.6354` n `8`; equity avg `-0.5634` n `158`; fx avg `-0.0544` n `6`; index avg `-0.1213` n `27`; metal avg `-0.2267` n `20`; unknown avg `0.0714` n `1209`
- 24h: commodity avg `-1.7781` n `13`; crypto_alt avg `0.4572` n `239`; crypto_major avg `1.8114` n `8`; equity avg `-2.2619` n `158`; fx avg `0.0101` n `6`; index avg `-0.0951` n `27`; metal avg `0.7335` n `20`; unknown avg `30.9003` n `1006`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2501`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1333`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
