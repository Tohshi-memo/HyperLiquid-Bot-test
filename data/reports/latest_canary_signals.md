# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T17:22:19.249025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2678` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.5458` n `228`; crypto_major avg `-0.3528` n `8`; equity avg `-0.0331` n `67`; fx avg `0.0092` n `6`; index avg `0.0322` n `23`; metal avg `0.0693` n `18`; unknown avg `0.1447` n `418`
- 1h: commodity avg `-0.1934` n `12`; crypto_alt avg `-0.4895` n `228`; crypto_major avg `-0.5966` n `8`; equity avg `0.177` n `67`; fx avg `0.0129` n `6`; index avg `0.0296` n `23`; metal avg `0.0544` n `18`; unknown avg `0.6444` n `418`
- 4h: commodity avg `0.023` n `12`; crypto_alt avg `-1.2191` n `228`; crypto_major avg `-0.8974` n `8`; equity avg `0.0599` n `67`; fx avg `-0.0029` n `6`; index avg `0.3704` n `23`; metal avg `-0.3639` n `18`; unknown avg `0.9726` n `416`
- 24h: commodity avg `1.2352` n `12`; crypto_alt avg `-2.1287` n `228`; crypto_major avg `-1.4892` n `8`; equity avg `-0.3372` n `67`; fx avg `-0.1093` n `6`; index avg `0.1359` n `23`; metal avg `-1.3726` n `18`; unknown avg `0.2941` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1762`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1671`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
