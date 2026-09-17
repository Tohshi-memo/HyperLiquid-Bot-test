# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T14:07:31.078048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0573` n `12`; crypto_alt avg `0.0273` n `234`; crypto_major avg `-0.0958` n `8`; equity avg `-0.5074` n `137`; fx avg `-0.002` n `6`; index avg `-0.0575` n `27`; metal avg `0.0326` n `20`; unknown avg `1.9876` n `903`
- 1h: commodity avg `0.2112` n `12`; crypto_alt avg `-0.1003` n `234`; crypto_major avg `-0.1741` n `8`; equity avg `-0.3673` n `137`; fx avg `0.0156` n `6`; index avg `-0.061` n `27`; metal avg `0.0994` n `20`; unknown avg `2.2261` n `899`
- 4h: commodity avg `0.0683` n `12`; crypto_alt avg `0.3156` n `234`; crypto_major avg `0.5055` n `8`; equity avg `0.278` n `137`; fx avg `-0.0701` n `6`; index avg `0.125` n `27`; metal avg `0.4589` n `20`; unknown avg `1.9722` n `893`
- 24h: commodity avg `-0.538` n `12`; crypto_alt avg `3.8389` n `234`; crypto_major avg `2.365` n `8`; equity avg `1.4199` n `137`; fx avg `0.0234` n `6`; index avg `0.2028` n `27`; metal avg `0.39` n `20`; unknown avg `0.5572` n `713`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
