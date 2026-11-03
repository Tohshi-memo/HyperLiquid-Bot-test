# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T01:22:27.942306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `13`; crypto_alt avg `0.0219` n `239`; crypto_major avg `0.0253` n `8`; equity avg `-0.0094` n `157`; fx avg `-0.0005` n `6`; index avg `0.0055` n `27`; metal avg `0.0485` n `20`; unknown avg `0.0588` n `1264`
- 1h: commodity avg `0.1367` n `13`; crypto_alt avg `-0.27` n `239`; crypto_major avg `0.0796` n `8`; equity avg `0.1778` n `157`; fx avg `-0.0006` n `6`; index avg `0.0576` n `27`; metal avg `-0.0427` n `20`; unknown avg `1.0823` n `1258`
- 4h: commodity avg `0.135` n `13`; crypto_alt avg `0.1913` n `239`; crypto_major avg `0.5609` n `8`; equity avg `0.5319` n `157`; fx avg `-0.0538` n `6`; index avg `0.0989` n `27`; metal avg `0.0545` n `20`; unknown avg `0.0562` n `1246`
- 24h: commodity avg `-1.2097` n `13`; crypto_alt avg `-3.0438` n `238`; crypto_major avg `-1.8513` n `8`; equity avg `-3.3387` n `157`; fx avg `0.1116` n `6`; index avg `-0.143` n `27`; metal avg `0.1372` n `20`; unknown avg `13.2035` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1683`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1657`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
