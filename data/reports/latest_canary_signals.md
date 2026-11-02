# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T07:52:25.626995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1551` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0216` n `13`; crypto_alt avg `0.1039` n `238`; crypto_major avg `0.0376` n `8`; equity avg `-0.0278` n `156`; fx avg `0.0065` n `6`; index avg `0.0039` n `27`; metal avg `0.0116` n `20`; unknown avg `0.0049` n `1240`
- 1h: commodity avg `-0.0541` n `13`; crypto_alt avg `-0.067` n `238`; crypto_major avg `-0.2258` n `8`; equity avg `-0.121` n `156`; fx avg `0.0177` n `6`; index avg `-0.0205` n `27`; metal avg `-0.0065` n `20`; unknown avg `-0.0127` n `1236`
- 4h: commodity avg `-0.0678` n `13`; crypto_alt avg `-1.4629` n `238`; crypto_major avg `-1.1772` n `8`; equity avg `-0.4689` n `156`; fx avg `0.0306` n `6`; index avg `-0.0221` n `27`; metal avg `0.0909` n `20`; unknown avg `0.142` n `1209`
- 24h: commodity avg `-0.4432` n `13`; crypto_alt avg `-1.9554` n `238`; crypto_major avg `-0.4651` n `8`; equity avg `0.9493` n `156`; fx avg `0.2433` n `6`; index avg `0.2969` n `27`; metal avg `0.1284` n `20`; unknown avg `2.3631` n `1071`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.196`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
