# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T21:52:30.501124+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `-0.101` n `238`; crypto_major avg `-0.1058` n `8`; equity avg `0.0007` n `156`; fx avg `0.0066` n `6`; index avg `-0.0367` n `27`; metal avg `0.005` n `20`; unknown avg `9.5304` n `1263`
- 1h: commodity avg `0.016` n `13`; crypto_alt avg `0.0291` n `238`; crypto_major avg `0.1009` n `8`; equity avg `0.0849` n `156`; fx avg `-0.0295` n `6`; index avg `-0.0054` n `27`; metal avg `0.0012` n `20`; unknown avg `22.7127` n `1249`
- 4h: commodity avg `0.0262` n `13`; crypto_alt avg `-0.5027` n `238`; crypto_major avg `-0.2144` n `8`; equity avg `-0.0462` n `156`; fx avg `-0.0363` n `6`; index avg `-0.0472` n `27`; metal avg `-0.0148` n `20`; unknown avg `166.3496` n `1207`
- 24h: commodity avg `0.0309` n `13`; crypto_alt avg `-0.5544` n `238`; crypto_major avg `-0.1094` n `8`; equity avg `0.3558` n `156`; fx avg `-0.0326` n `6`; index avg `0.0505` n `27`; metal avg `0.0406` n `20`; unknown avg `3.9485` n `1040`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
