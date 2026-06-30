# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T03:52:26.236959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.74` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.0612` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0351` n `12`; crypto_alt avg `-0.0688` n `228`; crypto_major avg `-0.1296` n `8`; equity avg `-0.0349` n `88`; fx avg `0.007` n `6`; index avg `-0.0031` n `23`; metal avg `-0.0029` n `20`; unknown avg `3.0743` n `765`
- 1h: commodity avg `-0.0575` n `12`; crypto_alt avg `-0.1622` n `228`; crypto_major avg `-0.336` n `8`; equity avg `0.0702` n `88`; fx avg `-0.0055` n `6`; index avg `0.0265` n `23`; metal avg `-0.0185` n `20`; unknown avg `5.483` n `765`
- 4h: commodity avg `0.0063` n `12`; crypto_alt avg `-0.5773` n `228`; crypto_major avg `-1.0336` n `8`; equity avg `0.1106` n `88`; fx avg `0.0343` n `6`; index avg `0.0276` n `23`; metal avg `-0.4934` n `20`; unknown avg `4.1328` n `763`
- 24h: commodity avg `-0.272` n `12`; crypto_alt avg `-0.3598` n `228`; crypto_major avg `0.7236` n `8`; equity avg `2.0617` n `88`; fx avg `0.1331` n `6`; index avg `0.3078` n `23`; metal avg `-0.8506` n `20`; unknown avg `4.2538` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
