# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T00:07:28.573290+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0048` n `13`; crypto_alt avg `0.0031` n `239`; crypto_major avg `0.0038` n `8`; equity avg `-0.0945` n `157`; fx avg `-0.0286` n `6`; index avg `-0.0281` n `27`; metal avg `0.0298` n `20`; unknown avg `11.9725` n `1252`
- 1h: commodity avg `-0.0323` n `13`; crypto_alt avg `0.012` n `239`; crypto_major avg `-0.0703` n `8`; equity avg `0.0261` n `157`; fx avg `-0.0021` n `6`; index avg `0.0275` n `27`; metal avg `0.0229` n `20`; unknown avg `207.2859` n `1250`
- 4h: commodity avg `-0.0241` n `13`; crypto_alt avg `0.207` n `239`; crypto_major avg `0.0789` n `8`; equity avg `-0.3326` n `157`; fx avg `-0.0296` n `6`; index avg `-0.0625` n `27`; metal avg `0.0044` n `20`; unknown avg `231.7231` n `1162`
- 24h: commodity avg `-1.4576` n `13`; crypto_alt avg `-2.8487` n `238`; crypto_major avg `-1.7793` n `8`; equity avg `-3.058` n `157`; fx avg `0.2127` n `6`; index avg `-0.0632` n `27`; metal avg `0.0868` n `20`; unknown avg `15.2795` n `1000`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
