# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T03:52:27.523087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.008` n `13`; crypto_alt avg `0.2953` n `239`; crypto_major avg `0.283` n `8`; equity avg `0.0261` n `157`; fx avg `0.0005` n `6`; index avg `-0.0171` n `27`; metal avg `-0.0483` n `20`; unknown avg `0.0683` n `1262`
- 1h: commodity avg `0.0429` n `13`; crypto_alt avg `-0.0441` n `239`; crypto_major avg `-0.0543` n `8`; equity avg `-0.3337` n `157`; fx avg `0.0044` n `6`; index avg `-0.0286` n `27`; metal avg `-0.2098` n `20`; unknown avg `-0.5934` n `1256`
- 4h: commodity avg `0.1558` n `13`; crypto_alt avg `-0.6843` n `239`; crypto_major avg `-0.1434` n `8`; equity avg `-0.237` n `157`; fx avg `-0.0859` n `6`; index avg `-0.0411` n `27`; metal avg `-0.2955` n `20`; unknown avg `4.117` n `1250`
- 24h: commodity avg `-0.9219` n `13`; crypto_alt avg `-3.7701` n `238`; crypto_major avg `-2.5283` n `8`; equity avg `-4.2164` n `157`; fx avg `-0.0303` n `6`; index avg `-0.2939` n `27`; metal avg `-0.1228` n `20`; unknown avg `12.1653` n `1018`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
