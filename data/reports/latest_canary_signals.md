# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T02:22:42.522301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `0.1846` n `239`; crypto_major avg `0.1803` n `8`; equity avg `-0.3019` n `163`; fx avg `-0.01` n `6`; index avg `-0.0319` n `27`; metal avg `0.0136` n `20`; unknown avg `1.4589` n `1264`
- 1h: commodity avg `-0.1374` n `13`; crypto_alt avg `-0.1638` n `239`; crypto_major avg `-0.3683` n `8`; equity avg `-1.215` n `163`; fx avg `-0.024` n `6`; index avg `-0.1469` n `27`; metal avg `-0.2173` n `20`; unknown avg `3.4846` n `1264`
- 4h: commodity avg `-0.1856` n `13`; crypto_alt avg `-0.0768` n `239`; crypto_major avg `0.0025` n `8`; equity avg `-0.4521` n `163`; fx avg `-0.0812` n `6`; index avg `-0.1139` n `27`; metal avg `-0.4803` n `20`; unknown avg `65.2316` n `1217`
- 24h: commodity avg `0.2152` n `13`; crypto_alt avg `0.5747` n `239`; crypto_major avg `0.6313` n `8`; equity avg `-0.45` n `163`; fx avg `-0.1139` n `6`; index avg `-0.1315` n `27`; metal avg `-0.6342` n `20`; unknown avg `7.0509` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
