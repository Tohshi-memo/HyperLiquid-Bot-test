# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T03:07:34.114591+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.4244` n `230`; crypto_major avg `0.4976` n `8`; equity avg `0.3022` n `98`; fx avg `-0.018` n `6`; index avg `0.0384` n `25`; metal avg `0.0713` n `20`; unknown avg `4.0656` n `771`
- 1h: commodity avg `0.021` n `12`; crypto_alt avg `0.4125` n `230`; crypto_major avg `0.4991` n `8`; equity avg `0.5448` n `98`; fx avg `-0.0358` n `6`; index avg `0.0648` n `25`; metal avg `0.2113` n `20`; unknown avg `2.1634` n `771`
- 4h: commodity avg `-0.0454` n `12`; crypto_alt avg `0.643` n `230`; crypto_major avg `0.8532` n `8`; equity avg `0.7246` n `98`; fx avg `0.0237` n `6`; index avg `0.2216` n `25`; metal avg `0.3306` n `20`; unknown avg `0.7656` n `770`
- 24h: commodity avg `-0.2679` n `12`; crypto_alt avg `1.7278` n `230`; crypto_major avg `1.6248` n `8`; equity avg `0.5237` n `98`; fx avg `-0.1357` n `6`; index avg `0.2099` n `25`; metal avg `0.2605` n `20`; unknown avg `0.0046` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1039`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0995`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.084`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
