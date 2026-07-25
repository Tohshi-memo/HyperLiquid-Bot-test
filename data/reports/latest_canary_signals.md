# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T03:22:32.858813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `-0.0204` n `230`; crypto_major avg `-0.0184` n `8`; equity avg `-0.0102` n `100`; fx avg `-0.0051` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.1771` n `774`
- 1h: commodity avg `-0.0867` n `12`; crypto_alt avg `0.0657` n `230`; crypto_major avg `0.0201` n `8`; equity avg `0.1856` n `100`; fx avg `-0.0067` n `6`; index avg `0.0343` n `25`; metal avg `-0.0032` n `20`; unknown avg `0.9866` n `774`
- 4h: commodity avg `-0.2097` n `12`; crypto_alt avg `-0.0004` n `230`; crypto_major avg `0.0794` n `8`; equity avg `0.2786` n `100`; fx avg `-0.0338` n `6`; index avg `0.0602` n `25`; metal avg `-0.0195` n `20`; unknown avg `0.1762` n `774`
- 24h: commodity avg `-0.5088` n `12`; crypto_alt avg `-1.2318` n `230`; crypto_major avg `-1.0883` n `8`; equity avg `-2.3097` n `100`; fx avg `-0.0487` n `6`; index avg `-0.1433` n `25`; metal avg `0.1922` n `20`; unknown avg `13.9704` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1175`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.11`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1022`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.102`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
