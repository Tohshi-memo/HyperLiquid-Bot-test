# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T21:22:30.444919+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `13`; crypto_alt avg `-0.14` n `238`; crypto_major avg `-0.0512` n `8`; equity avg `-0.0011` n `156`; fx avg `-0.0234` n `6`; index avg `0.0325` n `27`; metal avg `-0.0021` n `20`; unknown avg `3.7015` n `1263`
- 1h: commodity avg `-0.0029` n `13`; crypto_alt avg `0.2062` n `238`; crypto_major avg `0.2656` n `8`; equity avg `0.1248` n `156`; fx avg `-0.0223` n `6`; index avg `0.0274` n `27`; metal avg `0.0082` n `20`; unknown avg `21.7121` n `1249`
- 4h: commodity avg `0.0388` n `13`; crypto_alt avg `-0.6437` n `238`; crypto_major avg `-0.3798` n `8`; equity avg `-0.14` n `156`; fx avg `-0.0268` n `6`; index avg `-0.0227` n `27`; metal avg `-0.0233` n `20`; unknown avg `166.8521` n `1207`
- 24h: commodity avg `0.0417` n `13`; crypto_alt avg `-0.73` n `238`; crypto_major avg `-0.1345` n `8`; equity avg `0.3076` n `156`; fx avg `-0.0267` n `6`; index avg `0.0761` n `27`; metal avg `0.0402` n `20`; unknown avg `4.5492` n `1002`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
