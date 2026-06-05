# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T04:52:24.627200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.8729` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.7737` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `-0.1194` n `228`; crypto_major avg `-0.28` n `8`; equity avg `0.1604` n `74`; fx avg `-0.0029` n `6`; index avg `0.1205` n `23`; metal avg `0.0488` n `18`; unknown avg `-0.4502` n `424`
- 1h: commodity avg `0.0479` n `12`; crypto_alt avg `0.6153` n `228`; crypto_major avg `0.1214` n `8`; equity avg `0.3454` n `74`; fx avg `-0.0189` n `6`; index avg `0.1576` n `23`; metal avg `0.0915` n `18`; unknown avg `-0.4272` n `424`
- 4h: commodity avg `0.1765` n `12`; crypto_alt avg `-1.9693` n `228`; crypto_major avg `-1.6699` n `8`; equity avg `0.203` n `74`; fx avg `0.04` n `6`; index avg `0.1038` n `23`; metal avg `-0.4058` n `18`; unknown avg `-0.8537` n `424`
- 24h: commodity avg `-0.1542` n `12`; crypto_alt avg `-5.3371` n `228`; crypto_major avg `-4.9775` n `8`; equity avg `-1.4648` n `73`; fx avg `0.1836` n `6`; index avg `-0.5471` n `23`; metal avg `-0.7496` n `18`; unknown avg `-1.7688` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
