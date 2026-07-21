# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T01:07:31.930818+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0677` n `12`; crypto_alt avg `0.0217` n `230`; crypto_major avg `0.0401` n `8`; equity avg `0.1282` n `98`; fx avg `0.0111` n `6`; index avg `0.0187` n `25`; metal avg `0.0246` n `20`; unknown avg `-0.1622` n `771`
- 1h: commodity avg `-0.0421` n `12`; crypto_alt avg `0.3696` n `230`; crypto_major avg `0.4719` n `8`; equity avg `0.8155` n `98`; fx avg `0.0197` n `6`; index avg `0.2226` n `25`; metal avg `0.2019` n `20`; unknown avg `0.0353` n `771`
- 4h: commodity avg `-0.0293` n `12`; crypto_alt avg `0.1483` n `230`; crypto_major avg `0.1871` n `8`; equity avg `0.5107` n `98`; fx avg `0.031` n `6`; index avg `0.0776` n `25`; metal avg `0.1297` n `20`; unknown avg `-0.4494` n `770`
- 24h: commodity avg `-0.3428` n `12`; crypto_alt avg `1.6928` n `230`; crypto_major avg `1.4643` n `8`; equity avg `-0.0693` n `98`; fx avg `-0.1203` n `6`; index avg `-0.01` n `25`; metal avg `0.1821` n `20`; unknown avg `-0.052` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1007`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0868`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
