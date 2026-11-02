# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T10:07:34.577538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0287` n `13`; crypto_alt avg `-0.2106` n `238`; crypto_major avg `-0.2402` n `8`; equity avg `-0.0917` n `156`; fx avg `0.0053` n `6`; index avg `-0.0077` n `27`; metal avg `-0.0031` n `20`; unknown avg `0.1481` n `1258`
- 1h: commodity avg `0.048` n `13`; crypto_alt avg `-0.5899` n `238`; crypto_major avg `-0.5874` n `8`; equity avg `-0.0254` n `156`; fx avg `0.0009` n `6`; index avg `-0.0094` n `27`; metal avg `-0.0474` n `20`; unknown avg `2.0862` n `1258`
- 4h: commodity avg `-0.206` n `13`; crypto_alt avg `-1.0362` n `238`; crypto_major avg `-0.7284` n `8`; equity avg `-0.2233` n `156`; fx avg `0.1025` n `6`; index avg `-0.0386` n `27`; metal avg `-0.1171` n `20`; unknown avg `9.26` n `1168`
- 24h: commodity avg `-0.5407` n `13`; crypto_alt avg `-2.2732` n `238`; crypto_major avg `-0.7069` n `8`; equity avg `0.9085` n `156`; fx avg `0.2896` n `6`; index avg `0.2955` n `27`; metal avg `0.045` n `20`; unknown avg `4.8293` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
