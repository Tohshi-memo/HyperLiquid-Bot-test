# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T08:52:24.607755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0306` n `13`; crypto_alt avg `0.0146` n `239`; crypto_major avg `-0.145` n `8`; equity avg `-0.2228` n `158`; fx avg `0.0083` n `6`; index avg `-0.0894` n `27`; metal avg `0.0169` n `20`; unknown avg `158.0095` n `1265`
- 1h: commodity avg `-0.0137` n `13`; crypto_alt avg `0.6827` n `239`; crypto_major avg `0.442` n `8`; equity avg `-0.0208` n `158`; fx avg `0.0093` n `6`; index avg `-0.0326` n `27`; metal avg `0.0107` n `20`; unknown avg `0.4047` n `1243`
- 4h: commodity avg `0.3218` n `13`; crypto_alt avg `0.2083` n `239`; crypto_major avg `0.2113` n `8`; equity avg `-0.0518` n `158`; fx avg `-0.0266` n `6`; index avg `-0.0222` n `27`; metal avg `-0.1225` n `20`; unknown avg `0.1001` n `1211`
- 24h: commodity avg `-1.7489` n `13`; crypto_alt avg `0.8288` n `239`; crypto_major avg `1.7717` n `8`; equity avg `-2.6957` n `158`; fx avg `0.0112` n `6`; index avg `-0.1981` n `27`; metal avg `0.6788` n `20`; unknown avg `29.6082` n `1058`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2483`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1829`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1323`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
