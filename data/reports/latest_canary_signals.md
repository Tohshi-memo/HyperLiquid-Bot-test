# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T00:22:26.576656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.0295` n `230`; crypto_major avg `-0.009` n `8`; equity avg `-0.0379` n `96`; fx avg `0.0022` n `6`; index avg `-0.0082` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.1586` n `770`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `0.0384` n `230`; crypto_major avg `0.0004` n `8`; equity avg `-0.0362` n `96`; fx avg `0.0014` n `6`; index avg `-0.0219` n `25`; metal avg `0.0185` n `20`; unknown avg `0.0965` n `770`
- 4h: commodity avg `0.0186` n `12`; crypto_alt avg `0.1136` n `230`; crypto_major avg `-0.0296` n `8`; equity avg `0.0123` n `96`; fx avg `-0.0013` n `6`; index avg `-0.0123` n `25`; metal avg `0.0071` n `20`; unknown avg `0.0123` n `770`
- 24h: commodity avg `0.315` n `12`; crypto_alt avg `-0.2632` n `230`; crypto_major avg `0.4753` n `8`; equity avg `-0.2711` n `96`; fx avg `-0.0733` n `6`; index avg `0.0131` n `25`; metal avg `-0.0581` n `20`; unknown avg `0.0214` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
