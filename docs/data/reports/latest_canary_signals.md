# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T18:52:17.121921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5248` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3573` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0769` n `12`; crypto_alt avg `-0.7078` n `228`; crypto_major avg `-0.307` n `8`; equity avg `-0.0639` n `67`; fx avg `0.0013` n `6`; index avg `0.0115` n `23`; metal avg `-0.0072` n `18`; unknown avg `-0.0741` n `386`
- 1h: commodity avg `0.1273` n `12`; crypto_alt avg `-1.7084` n `228`; crypto_major avg `-0.9464` n `8`; equity avg `-0.3105` n `67`; fx avg `0.0068` n `6`; index avg `-0.0526` n `23`; metal avg `-0.0756` n `18`; unknown avg `-0.2328` n `386`
- 4h: commodity avg `-0.65` n `12`; crypto_alt avg `-1.5883` n `228`; crypto_major avg `-1.1549` n `8`; equity avg `-0.2755` n `67`; fx avg `0.064` n `6`; index avg `0.2024` n `23`; metal avg `0.3699` n `18`; unknown avg `-0.4581` n `386`
- 24h: commodity avg `-1.3401` n `12`; crypto_alt avg `-1.4446` n `228`; crypto_major avg `-1.2541` n `8`; equity avg `-0.1613` n `67`; fx avg `0.1799` n `6`; index avg `0.9037` n `23`; metal avg `-0.5691` n `18`; unknown avg `-0.8661` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0471`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0453`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0436`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0427`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0418`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0417`, n `668`, weak_sample_signal
