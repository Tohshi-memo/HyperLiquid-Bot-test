# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T13:37:28.996338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `12`; crypto_alt avg `0.0786` n `230`; crypto_major avg `0.1385` n `8`; equity avg `0.023` n `96`; fx avg `0.0075` n `6`; index avg `-0.009` n `25`; metal avg `0.0184` n `20`; unknown avg `0.008` n `770`
- 1h: commodity avg `-0.0178` n `12`; crypto_alt avg `0.0418` n `230`; crypto_major avg `-0.0489` n `8`; equity avg `0.0838` n `96`; fx avg `0.0068` n `6`; index avg `-0.0024` n `25`; metal avg `0.0404` n `20`; unknown avg `-0.0043` n `770`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `-0.1194` n `230`; crypto_major avg `-0.1148` n `8`; equity avg `0.0095` n `96`; fx avg `0.0127` n `6`; index avg `-0.0177` n `25`; metal avg `0.0133` n `20`; unknown avg `-0.0027` n `770`
- 24h: commodity avg `0.2054` n `12`; crypto_alt avg `0.5782` n `230`; crypto_major avg `1.1034` n `8`; equity avg `0.3376` n `96`; fx avg `-0.0018` n `6`; index avg `-0.0384` n `25`; metal avg `-0.0518` n `20`; unknown avg `0.1757` n `752`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1215`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1193`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0989`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0888`, n `666`, weak_sample_signal
