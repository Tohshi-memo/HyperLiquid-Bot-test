# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T18:52:24.175771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0509` n `13`; crypto_alt avg `-0.2658` n `238`; crypto_major avg `-0.328` n `8`; equity avg `-0.0524` n `156`; fx avg `-0.0042` n `6`; index avg `-0.0223` n `27`; metal avg `-0.0291` n `20`; unknown avg `0.9334` n `1261`
- 1h: commodity avg `-0.0311` n `13`; crypto_alt avg `-0.7964` n `238`; crypto_major avg `-0.8457` n `8`; equity avg `-0.4884` n `156`; fx avg `0.0167` n `6`; index avg `-0.0936` n `27`; metal avg `-0.0785` n `20`; unknown avg `0.6983` n `1255`
- 4h: commodity avg `0.0818` n `13`; crypto_alt avg `-0.8678` n `238`; crypto_major avg `-1.1193` n `8`; equity avg `-2.2762` n `156`; fx avg `0.0244` n `6`; index avg `-0.2815` n `27`; metal avg `-0.3351` n `20`; unknown avg `3.1553` n `1249`
- 24h: commodity avg `0.4469` n `13`; crypto_alt avg `-5.2487` n `238`; crypto_major avg `-5.0639` n `8`; equity avg `-6.5042` n `156`; fx avg `-0.0866` n `6`; index avg `-0.6165` n `27`; metal avg `-1.0624` n `20`; unknown avg `47.1631` n `1038`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.2015`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1986`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1915`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1807`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1623`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
