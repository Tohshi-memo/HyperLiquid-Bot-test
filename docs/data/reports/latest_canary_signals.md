# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T15:37:26.766924+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `-0.0122` n `230`; crypto_major avg `0.0095` n `8`; equity avg `0.0172` n `96`; fx avg `0.0038` n `6`; index avg `-0.0078` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0008` n `770`
- 1h: commodity avg `0.0327` n `12`; crypto_alt avg `0.0362` n `230`; crypto_major avg `-0.0008` n `8`; equity avg `-0.0471` n `96`; fx avg `0.0038` n `6`; index avg `-0.0116` n `25`; metal avg `-0.0063` n `20`; unknown avg `0.0406` n `770`
- 4h: commodity avg `0.0331` n `12`; crypto_alt avg `-0.0646` n `230`; crypto_major avg `-0.0732` n `8`; equity avg `-0.0448` n `96`; fx avg `0.0021` n `6`; index avg `-0.0203` n `25`; metal avg `0.011` n `20`; unknown avg `-0.0225` n `770`
- 24h: commodity avg `0.257` n `12`; crypto_alt avg `0.5253` n `230`; crypto_major avg `1.011` n `8`; equity avg `0.2727` n `96`; fx avg `0.0045` n `6`; index avg `-0.0376` n `25`; metal avg `-0.0292` n `20`; unknown avg `0.0874` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1344`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1289`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1022`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
