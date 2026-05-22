# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T05:37:14.877527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0306` n `12`; crypto_alt avg `-0.2169` n `228`; crypto_major avg `-0.0537` n `8`; equity avg `-0.0211` n `67`; fx avg `0.0109` n `6`; index avg `0.0263` n `23`; metal avg `0.2126` n `18`; unknown avg `-0.2391` n `386`
- 1h: commodity avg `0.1944` n `12`; crypto_alt avg `-0.1249` n `228`; crypto_major avg `-0.0515` n `8`; equity avg `0.0771` n `67`; fx avg `0.0201` n `6`; index avg `0.0335` n `23`; metal avg `0.192` n `18`; unknown avg `-0.2092` n `386`
- 4h: commodity avg `-0.0794` n `12`; crypto_alt avg `0.9176` n `228`; crypto_major avg `0.4465` n `8`; equity avg `0.4352` n `67`; fx avg `0.0603` n `6`; index avg `0.1955` n `23`; metal avg `0.4846` n `18`; unknown avg `-0.7768` n `386`
- 24h: commodity avg `-0.7223` n `12`; crypto_alt avg `1.9974` n `228`; crypto_major avg `0.3974` n `8`; equity avg `1.3379` n `66`; fx avg `0.1028` n `6`; index avg `0.6372` n `23`; metal avg `1.1465` n `18`; unknown avg `2.5696` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0475`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0473`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0461`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0433`, n `668`, weak_sample_signal
