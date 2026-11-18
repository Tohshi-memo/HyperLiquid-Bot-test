# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T07:52:31.519783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `0.341` n `239`; crypto_major avg `0.4844` n `8`; equity avg `0.4729` n `163`; fx avg `0.0027` n `6`; index avg `0.0691` n `27`; metal avg `0.0226` n `20`; unknown avg `0.8291` n `1266`
- 1h: commodity avg `0.0253` n `13`; crypto_alt avg `0.2514` n `239`; crypto_major avg `0.6272` n `8`; equity avg `0.5246` n `163`; fx avg `-0.0559` n `6`; index avg `0.0603` n `27`; metal avg `-0.1136` n `20`; unknown avg `0.5221` n `1264`
- 4h: commodity avg `-0.1769` n `13`; crypto_alt avg `0.3273` n `239`; crypto_major avg `0.5665` n `8`; equity avg `0.8088` n `163`; fx avg `-0.048` n `6`; index avg `0.0896` n `27`; metal avg `-0.2377` n `20`; unknown avg `0.8305` n `1224`
- 24h: commodity avg `-0.1333` n `13`; crypto_alt avg `0.405` n `239`; crypto_major avg `0.9748` n `8`; equity avg `1.065` n `163`; fx avg `-0.1376` n `6`; index avg `0.0822` n `27`; metal avg `-0.9711` n `20`; unknown avg `233.5613` n `1105`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
