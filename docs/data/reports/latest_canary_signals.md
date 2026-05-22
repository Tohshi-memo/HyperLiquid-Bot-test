# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T21:22:20.304730+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2088` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `0.1465` n `228`; crypto_major avg `0.1946` n `8`; equity avg `-0.0029` n `67`; fx avg `0.0033` n `6`; index avg `-0.0093` n `23`; metal avg `-0.0055` n `18`; unknown avg `-0.2357` n `386`
- 1h: commodity avg `0.3928` n `12`; crypto_alt avg `0.5297` n `228`; crypto_major avg `0.3645` n `8`; equity avg `-0.0418` n `67`; fx avg `-0.0076` n `6`; index avg `-0.0924` n `23`; metal avg `-0.057` n `18`; unknown avg `0.0298` n `386`
- 4h: commodity avg `0.1625` n `12`; crypto_alt avg `-2.1901` n `228`; crypto_major avg `-1.4892` n `8`; equity avg `-0.9212` n `67`; fx avg `0.0319` n `6`; index avg `-0.2804` n `23`; metal avg `-0.2662` n `18`; unknown avg `1.4062` n `386`
- 24h: commodity avg `-0.8614` n `12`; crypto_alt avg `-2.8141` n `228`; crypto_major avg `-2.0251` n `8`; equity avg `-1.0853` n `67`; fx avg `0.1879` n `6`; index avg `0.4556` n `23`; metal avg `-1.035` n `18`; unknown avg `-1.2828` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0504`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0467`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0466`, n `668`, weak_sample_signal
