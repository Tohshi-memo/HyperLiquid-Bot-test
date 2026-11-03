# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T04:37:32.531364+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `13`; crypto_alt avg `0.2146` n `239`; crypto_major avg `0.1807` n `8`; equity avg `0.09` n `157`; fx avg `-0.005` n `6`; index avg `0.0086` n `27`; metal avg `-0.035` n `20`; unknown avg `16.6677` n `1258`
- 1h: commodity avg `0.0378` n `13`; crypto_alt avg `0.7762` n `239`; crypto_major avg `0.5734` n `8`; equity avg `-0.204` n `157`; fx avg `-0.0007` n `6`; index avg `-0.0584` n `27`; metal avg `-0.1026` n `20`; unknown avg `0.2451` n `1198`
- 4h: commodity avg `0.1906` n `13`; crypto_alt avg `-0.4492` n `239`; crypto_major avg `-0.2967` n `8`; equity avg `-0.5874` n `157`; fx avg `-0.0488` n `6`; index avg `-0.0703` n `27`; metal avg `-0.4717` n `20`; unknown avg `0.3976` n `1198`
- 24h: commodity avg `-0.8528` n `13`; crypto_alt avg `-3.0031` n `238`; crypto_major avg `-2.0716` n `8`; equity avg `-4.4166` n `157`; fx avg `-0.0334` n `6`; index avg `-0.3652` n `27`; metal avg `-0.1761` n `20`; unknown avg `8.0309` n `964`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1652`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
