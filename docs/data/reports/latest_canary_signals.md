# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T05:07:33.042884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.001` n `12`; crypto_alt avg `0.0092` n `230`; crypto_major avg `0.0298` n `8`; equity avg `-0.1137` n `98`; fx avg `0.0073` n `6`; index avg `-0.0035` n `25`; metal avg `0.0077` n `20`; unknown avg `-0.088` n `773`
- 1h: commodity avg `-0.0294` n `12`; crypto_alt avg `0.2391` n `230`; crypto_major avg `0.0849` n `8`; equity avg `0.1472` n `98`; fx avg `0.0268` n `6`; index avg `0.0487` n `25`; metal avg `-0.0293` n `20`; unknown avg `-0.2491` n `773`
- 4h: commodity avg `0.0829` n `12`; crypto_alt avg `-0.4589` n `230`; crypto_major avg `-0.5427` n `8`; equity avg `-0.5126` n `98`; fx avg `-0.0054` n `6`; index avg `-0.083` n `25`; metal avg `0.0338` n `20`; unknown avg `0.4211` n `773`
- 24h: commodity avg `0.7363` n `12`; crypto_alt avg `-0.5531` n `230`; crypto_major avg `-0.7` n `8`; equity avg `-0.2103` n `98`; fx avg `-0.1395` n `6`; index avg `0.0346` n `25`; metal avg `-0.0921` n `20`; unknown avg `1.4788` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
