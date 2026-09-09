# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T21:17:05.969313+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2379` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `-0.1888` n `233`; crypto_major avg `-0.1732` n `8`; equity avg `-0.0429` n `134`; fx avg `0.009` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0069` n `20`; unknown avg `2.6076` n `797`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.1807` n `233`; crypto_major avg `-0.0734` n `8`; equity avg `-0.0722` n `134`; fx avg `0.0021` n `6`; index avg `0.0072` n `26`; metal avg `0.0458` n `20`; unknown avg `5.0474` n `767`
- 4h: commodity avg `0.1674` n `12`; crypto_alt avg `-1.7104` n `233`; crypto_major avg `-1.2472` n `8`; equity avg `-0.3611` n `134`; fx avg `-0.009` n `6`; index avg `-0.0093` n `26`; metal avg `-0.2169` n `20`; unknown avg `2.3801` n `745`
- 24h: commodity avg `0.1125` n `12`; crypto_alt avg `-1.5984` n `233`; crypto_major avg `-1.0869` n `8`; equity avg `-0.447` n `134`; fx avg `-0.0177` n `6`; index avg `-0.1139` n `26`; metal avg `0.4973` n `20`; unknown avg `152.1351` n `699`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
