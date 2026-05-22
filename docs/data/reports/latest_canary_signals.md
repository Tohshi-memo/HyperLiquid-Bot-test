# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T20:07:17.513508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3485` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0767` n `12`; crypto_alt avg `0.1336` n `228`; crypto_major avg `0.0116` n `8`; equity avg `0.0213` n `67`; fx avg `-0.006` n `6`; index avg `0.0268` n `23`; metal avg `-0.0993` n `18`; unknown avg `-0.0434` n `386`
- 1h: commodity avg `-0.0648` n `12`; crypto_alt avg `-0.3881` n `228`; crypto_major avg `-0.2313` n `8`; equity avg `-0.3434` n `67`; fx avg `0.005` n `6`; index avg `-0.17` n `23`; metal avg `-0.1364` n `18`; unknown avg `0.3792` n `386`
- 4h: commodity avg `-0.2188` n `12`; crypto_alt avg `-2.5625` n `228`; crypto_major avg `-1.5093` n `8`; equity avg `-0.9436` n `67`; fx avg `0.0589` n `6`; index avg `-0.1608` n `23`; metal avg `-0.3024` n `18`; unknown avg `0.4528` n `386`
- 24h: commodity avg `-1.0801` n `12`; crypto_alt avg `-2.9954` n `228`; crypto_major avg `-2.3147` n `8`; equity avg `-1.1443` n `67`; fx avg `0.1804` n `6`; index avg `0.549` n `23`; metal avg `-1.088` n `18`; unknown avg `-1.4401` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0511`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0496`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
