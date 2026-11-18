# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T05:37:30.176148+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `13`; crypto_alt avg `0.1102` n `239`; crypto_major avg `0.0306` n `8`; equity avg `-0.1188` n `163`; fx avg `-0.0028` n `6`; index avg `-0.0171` n `27`; metal avg `-0.0466` n `20`; unknown avg `0.3939` n `1266`
- 1h: commodity avg `-0.0299` n `13`; crypto_alt avg `0.3219` n `239`; crypto_major avg `0.4287` n `8`; equity avg `0.2261` n `163`; fx avg `0.0055` n `6`; index avg `0.0124` n `27`; metal avg `0.075` n `20`; unknown avg `1.1023` n `1262`
- 4h: commodity avg `-0.1426` n `13`; crypto_alt avg `0.0814` n `239`; crypto_major avg `0.4984` n `8`; equity avg `-0.0524` n `163`; fx avg `-0.0108` n `6`; index avg `0.0289` n `27`; metal avg `-0.3712` n `20`; unknown avg `4.5113` n `1252`
- 24h: commodity avg `0.2113` n `13`; crypto_alt avg `-0.1871` n `239`; crypto_major avg `0.3457` n `8`; equity avg `0.1532` n `163`; fx avg `-0.09` n `6`; index avg `0.0014` n `27`; metal avg `-0.8978` n `20`; unknown avg `492.7106` n `1073`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
