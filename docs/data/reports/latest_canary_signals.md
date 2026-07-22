# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T07:52:29.576511+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0639` n `12`; crypto_alt avg `0.0552` n `230`; crypto_major avg `0.0713` n `8`; equity avg `-0.0462` n `98`; fx avg `-0.0103` n `6`; index avg `-0.0202` n `25`; metal avg `-0.0871` n `20`; unknown avg `-0.038` n `772`
- 1h: commodity avg `0.2537` n `12`; crypto_alt avg `-0.0929` n `230`; crypto_major avg `-0.1741` n `8`; equity avg `-0.1731` n `98`; fx avg `-0.0065` n `6`; index avg `-0.0453` n `25`; metal avg `-0.0644` n `20`; unknown avg `-0.0646` n `772`
- 4h: commodity avg `0.4214` n `12`; crypto_alt avg `-0.8595` n `230`; crypto_major avg `-1.2323` n `8`; equity avg `-1.1987` n `98`; fx avg `-0.0664` n `6`; index avg `-0.2692` n `25`; metal avg `-0.2325` n `20`; unknown avg `-0.2402` n `739`
- 24h: commodity avg `0.9864` n `12`; crypto_alt avg `-1.2738` n `230`; crypto_major avg `-1.7989` n `8`; equity avg `0.6204` n `98`; fx avg `-0.0104` n `6`; index avg `-0.0159` n `25`; metal avg `0.2016` n `20`; unknown avg `0.0063` n `739`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1036`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0844`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.072`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.072`, n `666`, weak_sample_signal
