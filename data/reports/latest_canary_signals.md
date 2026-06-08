# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T06:52:23.942509+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1609` n `12`; crypto_alt avg `-0.1375` n `228`; crypto_major avg `0.109` n `8`; equity avg `-0.0406` n `74`; fx avg `0.0014` n `6`; index avg `0.0935` n `23`; metal avg `0.2549` n `18`; unknown avg `0.051` n `517`
- 1h: commodity avg `-0.1214` n `12`; crypto_alt avg `0.7917` n `228`; crypto_major avg `0.8116` n `8`; equity avg `0.19` n `74`; fx avg `-0.101` n `6`; index avg `0.0752` n `23`; metal avg `0.4459` n `18`; unknown avg `0.0092` n `507`
- 4h: commodity avg `0.1991` n `12`; crypto_alt avg `-0.211` n `228`; crypto_major avg `-0.3794` n `8`; equity avg `-1.1485` n `74`; fx avg `-0.1853` n `6`; index avg `-0.2372` n `23`; metal avg `-0.3007` n `18`; unknown avg `-0.1921` n `507`
- 24h: commodity avg `0.6526` n `12`; crypto_alt avg `-0.0896` n `228`; crypto_major avg `1.743` n `8`; equity avg `0.0226` n `74`; fx avg `-0.2801` n `6`; index avg `-0.0554` n `23`; metal avg `-0.6644` n `18`; unknown avg `-5.549` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
