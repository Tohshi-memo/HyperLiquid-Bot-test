# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T14:52:29.501445+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.004` n `12`; crypto_alt avg `0.1112` n `230`; crypto_major avg `0.1519` n `8`; equity avg `0.0384` n `100`; fx avg `-0.0103` n `6`; index avg `0.01` n `25`; metal avg `0.0187` n `20`; unknown avg `13.5543` n `773`
- 1h: commodity avg `0.0036` n `12`; crypto_alt avg `-0.0953` n `230`; crypto_major avg `0.064` n `8`; equity avg `-0.5277` n `100`; fx avg `-0.011` n `6`; index avg `-0.0212` n `25`; metal avg `0.0234` n `20`; unknown avg `13.4664` n `773`
- 4h: commodity avg `0.0608` n `12`; crypto_alt avg `-1.1877` n `230`; crypto_major avg `-1.1471` n `8`; equity avg `-2.5485` n `100`; fx avg `-0.0242` n `6`; index avg `-0.2384` n `25`; metal avg `-0.0822` n `20`; unknown avg `13.271` n `773`
- 24h: commodity avg `-0.3429` n `12`; crypto_alt avg `-2.0097` n `230`; crypto_major avg `-1.7687` n `8`; equity avg `-2.9887` n `100`; fx avg `-0.1446` n `6`; index avg `-0.3443` n `25`; metal avg `-0.0844` n `20`; unknown avg `13.8652` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1588`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1246`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1205`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1057`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1048`, n `666`, weak_sample_signal
