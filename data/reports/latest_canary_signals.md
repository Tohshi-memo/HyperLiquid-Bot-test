# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T11:07:29.428224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0022` n `12`; crypto_alt avg `0.0026` n `230`; crypto_major avg `0.0625` n `8`; equity avg `-0.0063` n `96`; fx avg `0.0007` n `6`; index avg `-0.0021` n `25`; metal avg `-0.0059` n `20`; unknown avg `-0.0061` n `770`
- 1h: commodity avg `-0.013` n `12`; crypto_alt avg `0.1661` n `230`; crypto_major avg `0.2154` n `8`; equity avg `0.0356` n `96`; fx avg `0.0189` n `6`; index avg `-0.0008` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0794` n `770`
- 4h: commodity avg `0.0286` n `12`; crypto_alt avg `0.1025` n `230`; crypto_major avg `0.1579` n `8`; equity avg `0.0329` n `96`; fx avg `0.0094` n `6`; index avg `0.0294` n `25`; metal avg `-0.0566` n `20`; unknown avg `0.0112` n `770`
- 24h: commodity avg `0.1799` n `12`; crypto_alt avg `0.5784` n `230`; crypto_major avg `1.1667` n `8`; equity avg `0.2049` n `96`; fx avg `0.0009` n `6`; index avg `-0.0405` n `25`; metal avg `-0.0842` n `20`; unknown avg `0.1316` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1122`, n `667`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1116`, n `667`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `667`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `667`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
