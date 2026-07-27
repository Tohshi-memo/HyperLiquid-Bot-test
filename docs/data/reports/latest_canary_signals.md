# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T11:37:33.687550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0534` n `12`; crypto_alt avg `0.0309` n `230`; crypto_major avg `-0.1083` n `8`; equity avg `-0.2209` n `100`; fx avg `0.007` n `6`; index avg `-0.0208` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.015` n `776`
- 1h: commodity avg `0.0445` n `12`; crypto_alt avg `-0.0226` n `230`; crypto_major avg `-0.1768` n `8`; equity avg `-0.429` n `100`; fx avg `0.0015` n `6`; index avg `-0.0478` n `25`; metal avg `-0.024` n `20`; unknown avg `0.0035` n `775`
- 4h: commodity avg `-0.1686` n `12`; crypto_alt avg `-0.2809` n `230`; crypto_major avg `-0.1443` n `8`; equity avg `-0.3068` n `100`; fx avg `-0.0135` n `6`; index avg `-0.0197` n `25`; metal avg `-0.0418` n `20`; unknown avg `-0.1897` n `775`
- 24h: commodity avg `-0.5783` n `12`; crypto_alt avg `0.5007` n `230`; crypto_major avg `1.1291` n `8`; equity avg `0.8247` n `100`; fx avg `0.0967` n `6`; index avg `0.1089` n `25`; metal avg `0.3622` n `20`; unknown avg `-0.1679` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1943`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
