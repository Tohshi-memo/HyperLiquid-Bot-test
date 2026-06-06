# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T15:07:22.081074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0808` n `12`; crypto_alt avg `-0.766` n `228`; crypto_major avg `-0.9496` n `8`; equity avg `-0.1648` n `74`; fx avg `-0.0048` n `6`; index avg `-0.0582` n `23`; metal avg `-0.0159` n `18`; unknown avg `-2.6138` n `515`
- 1h: commodity avg `0.0519` n `12`; crypto_alt avg `-0.6697` n `228`; crypto_major avg `-0.7452` n `8`; equity avg `-0.0514` n `74`; fx avg `-0.0014` n `6`; index avg `0.0277` n `23`; metal avg `-0.1799` n `18`; unknown avg `-2.1085` n `515`
- 4h: commodity avg `0.0743` n `12`; crypto_alt avg `0.1135` n `228`; crypto_major avg `-0.2149` n `8`; equity avg `0.5993` n `74`; fx avg `0.0036` n `6`; index avg `0.4288` n `23`; metal avg `-0.1562` n `18`; unknown avg `0.0146` n `411`
- 24h: commodity avg `-0.2692` n `12`; crypto_alt avg `-2.401` n `228`; crypto_major avg `-2.1885` n `8`; equity avg `-3.804` n `74`; fx avg `-0.1284` n `6`; index avg `-2.2072` n `23`; metal avg `-2.0991` n `18`; unknown avg `-0.4164` n `400`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
