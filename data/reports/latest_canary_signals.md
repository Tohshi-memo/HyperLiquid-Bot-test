# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T18:37:27.074501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0163` n `12`; crypto_alt avg `-0.2367` n `230`; crypto_major avg `-0.3146` n `8`; equity avg `-0.0771` n `98`; fx avg `-0.0003` n `6`; index avg `-0.0042` n `25`; metal avg `-0.0092` n `20`; unknown avg `-0.0026` n `773`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-0.4868` n `230`; crypto_major avg `-0.4532` n `8`; equity avg `-0.4974` n `98`; fx avg `0.0086` n `6`; index avg `-0.0618` n `25`; metal avg `-0.0404` n `20`; unknown avg `0.1048` n `773`
- 4h: commodity avg `0.0892` n `12`; crypto_alt avg `-0.3033` n `230`; crypto_major avg `-0.1194` n `8`; equity avg `-0.5154` n `98`; fx avg `0.0045` n `6`; index avg `0.0116` n `25`; metal avg `-0.1977` n `20`; unknown avg `-0.2053` n `773`
- 24h: commodity avg `0.6349` n `12`; crypto_alt avg `-0.5682` n `230`; crypto_major avg `-0.8736` n `8`; equity avg `-0.6782` n `98`; fx avg `-0.0307` n `6`; index avg `-0.1305` n `25`; metal avg `0.2348` n `20`; unknown avg `0.7241` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0721`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0716`, n `666`, weak_sample_signal
