# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T20:52:26.033429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `12`; crypto_alt avg `-0.0105` n `230`; crypto_major avg `0.0396` n `8`; equity avg `0.007` n `100`; fx avg `-0.0015` n `6`; index avg `0.0028` n `25`; metal avg `0.0032` n `20`; unknown avg `0.0271` n `774`
- 1h: commodity avg `-0.0064` n `12`; crypto_alt avg `-0.1186` n `230`; crypto_major avg `-0.134` n `8`; equity avg `0.0236` n `100`; fx avg `0.0023` n `6`; index avg `0.0232` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0971` n `774`
- 4h: commodity avg `-0.0645` n `12`; crypto_alt avg `0.1008` n `230`; crypto_major avg `0.2086` n `8`; equity avg `0.2325` n `100`; fx avg `0.0041` n `6`; index avg `0.0851` n `25`; metal avg `0.0298` n `20`; unknown avg `-0.1222` n `774`
- 24h: commodity avg `-0.6543` n `12`; crypto_alt avg `0.4014` n `230`; crypto_major avg `1.0324` n `8`; equity avg `0.3105` n `100`; fx avg `0.0079` n `6`; index avg `0.1528` n `25`; metal avg `0.0212` n `20`; unknown avg `-0.3393` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1341`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1203`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1159`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1136`, n `666`, weak_sample_signal
