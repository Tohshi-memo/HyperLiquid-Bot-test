# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T03:37:26.409529+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0467` n `12`; crypto_alt avg `0.0357` n `230`; crypto_major avg `0.0716` n `8`; equity avg `0.161` n `98`; fx avg `0.0013` n `6`; index avg `0.036` n `25`; metal avg `-0.0201` n `20`; unknown avg `-0.1163` n `773`
- 1h: commodity avg `0.0407` n `12`; crypto_alt avg `-0.1737` n `230`; crypto_major avg `0.0288` n `8`; equity avg `0.1931` n `98`; fx avg `0.0105` n `6`; index avg `0.027` n `25`; metal avg `0.0885` n `20`; unknown avg `-0.1006` n `773`
- 4h: commodity avg `0.1439` n `12`; crypto_alt avg `-0.3259` n `230`; crypto_major avg `-0.2137` n `8`; equity avg `0.0202` n `98`; fx avg `-0.0627` n `6`; index avg `0.033` n `25`; metal avg `0.1889` n `20`; unknown avg `-0.1504` n `773`
- 24h: commodity avg `0.7745` n `12`; crypto_alt avg `-0.8109` n `230`; crypto_major avg `-0.6381` n `8`; equity avg `-0.6671` n `98`; fx avg `-0.1455` n `6`; index avg `-0.1163` n `25`; metal avg `-0.0958` n `20`; unknown avg `1.756` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0949`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
