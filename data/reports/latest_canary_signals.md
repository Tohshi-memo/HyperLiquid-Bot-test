# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T05:22:30.484154+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0379` n `230`; crypto_major avg `-0.0347` n `8`; equity avg `0.0681` n `100`; fx avg `-0.021` n `6`; index avg `0.0229` n `25`; metal avg `0.0159` n `20`; unknown avg `-0.2807` n `772`
- 1h: commodity avg `-0.0327` n `12`; crypto_alt avg `0.053` n `230`; crypto_major avg `0.0325` n `8`; equity avg `0.4557` n `100`; fx avg `-0.0147` n `6`; index avg `0.088` n `25`; metal avg `0.0277` n `20`; unknown avg `-0.0053` n `772`
- 4h: commodity avg `0.0636` n `12`; crypto_alt avg `0.4088` n `230`; crypto_major avg `0.2395` n `8`; equity avg `-0.2573` n `100`; fx avg `-0.0308` n `6`; index avg `-0.099` n `25`; metal avg `-0.08` n `20`; unknown avg `-0.219` n `772`
- 24h: commodity avg `0.489` n `12`; crypto_alt avg `-0.9984` n `230`; crypto_major avg `-1.6945` n `8`; equity avg `-1.8382` n `99`; fx avg `-0.1241` n `6`; index avg `-0.5364` n `25`; metal avg `-0.9587` n `20`; unknown avg `0.0458` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1714`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1067`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0921`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0884`, n `666`, weak_sample_signal
