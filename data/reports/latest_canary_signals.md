# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T10:37:35.594524+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1139` n `13`; crypto_alt avg `-0.077` n `239`; crypto_major avg `0.1313` n `8`; equity avg `0.0474` n `158`; fx avg `0.0049` n `6`; index avg `0.0251` n `27`; metal avg `0.0216` n `20`; unknown avg `0.0938` n `1256`
- 1h: commodity avg `0.2326` n `13`; crypto_alt avg `0.2235` n `239`; crypto_major avg `0.0076` n `8`; equity avg `-0.3505` n `158`; fx avg `0.0085` n `6`; index avg `-0.0329` n `27`; metal avg `-0.1121` n `20`; unknown avg `-0.0996` n `1250`
- 4h: commodity avg `-0.2505` n `13`; crypto_alt avg `0.6011` n `239`; crypto_major avg `0.427` n `8`; equity avg `1.5112` n `158`; fx avg `-0.081` n `6`; index avg `0.2334` n `27`; metal avg `0.135` n `20`; unknown avg `182.6419` n `1194`
- 24h: commodity avg `0.7392` n `13`; crypto_alt avg `-3.2959` n `239`; crypto_major avg `-5.3061` n `8`; equity avg `-4.8915` n `158`; fx avg `-0.0451` n `6`; index avg `-0.6279` n `27`; metal avg `-0.3589` n `20`; unknown avg `225.7117` n `1081`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2236`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1599`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
