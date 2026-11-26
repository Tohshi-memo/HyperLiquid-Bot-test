# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T06:22:32.338089+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `13`; crypto_alt avg `-0.2388` n `239`; crypto_major avg `-0.2089` n `8`; equity avg `-0.2293` n `168`; fx avg `0.0073` n `6`; index avg `-0.0309` n `27`; metal avg `-0.0766` n `20`; unknown avg `11.6586` n `1265`
- 1h: commodity avg `-0.0994` n `13`; crypto_alt avg `-0.2671` n `239`; crypto_major avg `-0.6841` n `8`; equity avg `-0.85` n `168`; fx avg `0.0144` n `6`; index avg `-0.1005` n `27`; metal avg `-0.2738` n `20`; unknown avg `0.3744` n `1243`
- 4h: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.6873` n `239`; crypto_major avg `-0.7403` n `8`; equity avg `-0.8538` n `168`; fx avg `0.0094` n `6`; index avg `-0.0871` n `27`; metal avg `-0.1582` n `20`; unknown avg `0.6386` n `1227`
- 24h: commodity avg `0.5664` n `13`; crypto_alt avg `2.5118` n `239`; crypto_major avg `2.5054` n `8`; equity avg `2.046` n `168`; fx avg `0.026` n `6`; index avg `0.1218` n `27`; metal avg `0.62` n `20`; unknown avg `764.2753` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
