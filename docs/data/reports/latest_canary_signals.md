# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T03:22:30.343288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0305` n `12`; crypto_alt avg `-0.1879` n `230`; crypto_major avg `-0.1524` n `8`; equity avg `-0.048` n `96`; fx avg `-0.0021` n `6`; index avg `0.001` n `25`; metal avg `0.0152` n `20`; unknown avg `0.3933` n `770`
- 1h: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.2188` n `230`; crypto_major avg `-0.2207` n `8`; equity avg `-0.0531` n `96`; fx avg `-0.0113` n `6`; index avg `0.0374` n `25`; metal avg `0.0058` n `20`; unknown avg `0.0569` n `770`
- 4h: commodity avg `-0.0741` n `12`; crypto_alt avg `-0.152` n `230`; crypto_major avg `0.0681` n `8`; equity avg `0.1231` n `96`; fx avg `0.045` n `6`; index avg `0.0087` n `25`; metal avg `0.0616` n `20`; unknown avg `0.0282` n `770`
- 24h: commodity avg `0.2848` n `12`; crypto_alt avg `-0.278` n `230`; crypto_major avg `0.6191` n `8`; equity avg `-0.267` n `96`; fx avg `-0.0221` n `6`; index avg `0.0094` n `25`; metal avg `-0.0117` n `20`; unknown avg `0.0469` n `737`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
