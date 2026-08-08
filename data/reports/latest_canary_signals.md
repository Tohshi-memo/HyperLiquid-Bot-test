# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T09:58:49.877588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.0167` n `230`; crypto_major avg `-0.0609` n `8`; equity avg `0.0078` n `112`; fx avg `0.0008` n `6`; index avg `0.0034` n `25`; metal avg `0.0066` n `20`; unknown avg `-0.0511` n `784`
- 1h: commodity avg `0.0049` n `12`; crypto_alt avg `0.059` n `230`; crypto_major avg `0.0376` n `8`; equity avg `0.0504` n `112`; fx avg `0.009` n `6`; index avg `0.0019` n `25`; metal avg `0.0342` n `20`; unknown avg `-0.0497` n `784`
- 4h: commodity avg `0.0125` n `12`; crypto_alt avg `0.2644` n `230`; crypto_major avg `0.2427` n `8`; equity avg `0.0566` n `112`; fx avg `0.0036` n `6`; index avg `0.0114` n `25`; metal avg `0.036` n `20`; unknown avg `0.1323` n `752`
- 24h: commodity avg `0.0084` n `12`; crypto_alt avg `0.018` n `230`; crypto_major avg `0.0678` n `8`; equity avg `0.7069` n `112`; fx avg `-0.0141` n `6`; index avg `0.0403` n `25`; metal avg `-0.1692` n `20`; unknown avg `-0.0625` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
