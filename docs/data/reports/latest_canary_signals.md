# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T23:37:33.182777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2801` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0069` n `12`; crypto_alt avg `0.0167` n `228`; crypto_major avg `-0.0677` n `8`; equity avg `0.0261` n `77`; fx avg `-0.0455` n `6`; index avg `0.0447` n `23`; metal avg `0.0295` n `18`; unknown avg `-0.1114` n `687`
- 1h: commodity avg `0.1043` n `12`; crypto_alt avg `-0.1998` n `228`; crypto_major avg `-0.4451` n `8`; equity avg `-0.0072` n `77`; fx avg `-0.0359` n `6`; index avg `0.0027` n `23`; metal avg `0.0824` n `18`; unknown avg `0.5222` n `687`
- 4h: commodity avg `-0.0349` n `12`; crypto_alt avg `-0.8283` n `228`; crypto_major avg `-1.3674` n `8`; equity avg `-0.0554` n `77`; fx avg `-0.0312` n `6`; index avg `-0.0873` n `23`; metal avg `-0.1014` n `18`; unknown avg `0.6744` n `679`
- 24h: commodity avg `0.4872` n `12`; crypto_alt avg `0.8181` n `228`; crypto_major avg `1.9523` n `8`; equity avg `1.7621` n `76`; fx avg `-0.1239` n `6`; index avg `0.9489` n `23`; metal avg `0.4406` n `18`; unknown avg `1.9819` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
