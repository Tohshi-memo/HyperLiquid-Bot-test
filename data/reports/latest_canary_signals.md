# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T02:22:28.155876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.1631` n `230`; crypto_major avg `-0.2039` n `8`; equity avg `-0.1758` n `98`; fx avg `0.0002` n `6`; index avg `-0.0474` n `25`; metal avg `0.0174` n `20`; unknown avg `0.2077` n `771`
- 1h: commodity avg `0.0156` n `12`; crypto_alt avg `-0.2204` n `230`; crypto_major avg `-0.1986` n `8`; equity avg `-0.5214` n `98`; fx avg `-0.0006` n `6`; index avg `-0.0127` n `25`; metal avg `-0.0432` n `20`; unknown avg `-0.0015` n `771`
- 4h: commodity avg `-0.0538` n `12`; crypto_alt avg `0.1212` n `230`; crypto_major avg `0.1422` n `8`; equity avg `0.1156` n `98`; fx avg `0.0609` n `6`; index avg `0.1317` n `25`; metal avg `0.1475` n `20`; unknown avg `-0.5621` n `770`
- 24h: commodity avg `-0.3598` n `12`; crypto_alt avg `1.3235` n `230`; crypto_major avg `1.1281` n `8`; equity avg `0.1017` n `98`; fx avg `-0.0914` n `6`; index avg `0.1301` n `25`; metal avg `0.1792` n `20`; unknown avg `-0.0839` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1025`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0994`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0924`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0786`, n `666`, weak_sample_signal
