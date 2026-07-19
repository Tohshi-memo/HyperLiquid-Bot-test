# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T23:22:29.133888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.0976` n `230`; crypto_major avg `0.0083` n `8`; equity avg `-0.0012` n `98`; fx avg `-0.0018` n `6`; index avg `-0.0122` n `25`; metal avg `-0.0247` n `20`; unknown avg `0.1252` n `769`
- 1h: commodity avg `-0.0646` n `12`; crypto_alt avg `-0.1991` n `230`; crypto_major avg `-0.1911` n `8`; equity avg `-0.1029` n `98`; fx avg `0.0051` n `6`; index avg `-0.0214` n `25`; metal avg `-0.0199` n `20`; unknown avg `0.1277` n `769`
- 4h: commodity avg `0.0053` n `12`; crypto_alt avg `0.2316` n `230`; crypto_major avg `0.3183` n `8`; equity avg `0.1809` n `98`; fx avg `0.0147` n `6`; index avg `0.0754` n `25`; metal avg `-0.1455` n `20`; unknown avg `-0.0238` n `769`
- 24h: commodity avg `-0.0829` n `12`; crypto_alt avg `-0.1643` n `230`; crypto_major avg `0.249` n `8`; equity avg `0.4788` n `97`; fx avg `0.0813` n `6`; index avg `-0.0027` n `25`; metal avg `-0.1198` n `20`; unknown avg `-0.0107` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1477`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1422`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1366`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1267`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1074`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0968`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0954`, n `666`, weak_sample_signal
