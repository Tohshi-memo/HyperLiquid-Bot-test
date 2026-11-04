# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T07:07:28.699733+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.04` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0208` n `13`; crypto_alt avg `-0.1975` n `239`; crypto_major avg `-0.194` n `8`; equity avg `-0.0992` n `158`; fx avg `-0.0033` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0332` n `20`; unknown avg `-0.0461` n `1258`
- 1h: commodity avg `0.0175` n `13`; crypto_alt avg `0.3052` n `239`; crypto_major avg `0.0268` n `8`; equity avg `-0.0768` n `158`; fx avg `0.0148` n `6`; index avg `0.0111` n `27`; metal avg `0.0895` n `20`; unknown avg `-0.0607` n `1256`
- 4h: commodity avg `0.3865` n `13`; crypto_alt avg `3.0854` n `239`; crypto_major avg `2.3541` n `8`; equity avg `3.2461` n `158`; fx avg `0.0585` n `6`; index avg `0.5224` n `27`; metal avg `0.9811` n `20`; unknown avg `2.5497` n `1236`
- 24h: commodity avg `-0.268` n `13`; crypto_alt avg `2.711` n `239`; crypto_major avg `1.397` n `8`; equity avg `2.6061` n `158`; fx avg `0.1624` n `6`; index avg `0.1527` n `27`; metal avg `0.7742` n `20`; unknown avg `191.4218` n `1053`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2333`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1445`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
