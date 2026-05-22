# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T19:37:21.164063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7658` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7167` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.7933` n `228`; crypto_major avg `-0.4796` n `8`; equity avg `-0.0237` n `67`; fx avg `-0.0002` n `6`; index avg `-0.0093` n `23`; metal avg `0.0193` n `18`; unknown avg `0.5686` n `386`
- 1h: commodity avg `0.1204` n `12`; crypto_alt avg `-1.8666` n `228`; crypto_major avg `-1.0718` n `8`; equity avg `-0.4851` n `67`; fx avg `0.0277` n `6`; index avg `-0.1433` n `23`; metal avg `-0.1935` n `18`; unknown avg `0.8887` n `386`
- 4h: commodity avg `-0.1254` n `12`; crypto_alt avg `-2.8589` n `228`; crypto_major avg `-1.8638` n `8`; equity avg `-0.7492` n `67`; fx avg `0.0825` n `6`; index avg `-0.098` n `23`; metal avg `-0.1471` n `18`; unknown avg `0.0285` n `386`
- 24h: commodity avg `-0.6782` n `12`; crypto_alt avg `-2.8833` n `228`; crypto_major avg `-2.2234` n `8`; equity avg `-0.7337` n `67`; fx avg `0.1844` n `6`; index avg `0.6539` n `23`; metal avg `-0.9438` n `18`; unknown avg `-0.9713` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0499`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0447`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
