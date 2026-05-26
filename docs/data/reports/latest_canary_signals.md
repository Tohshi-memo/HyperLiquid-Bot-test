# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T20:07:18.974929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0089` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.005` n `12`; crypto_alt avg `0.0285` n `228`; crypto_major avg `-0.1679` n `8`; equity avg `-0.0421` n `67`; fx avg `-0.0006` n `6`; index avg `-0.1188` n `23`; metal avg `-0.001` n `18`; unknown avg `-0.0435` n `418`
- 1h: commodity avg `-0.0351` n `12`; crypto_alt avg `0.3285` n `228`; crypto_major avg `0.1273` n `8`; equity avg `0.0456` n `67`; fx avg `0.0055` n `6`; index avg `0.023` n `23`; metal avg `0.2518` n `18`; unknown avg `-0.3502` n `418`
- 4h: commodity avg `-0.4233` n `12`; crypto_alt avg `-0.9055` n `228`; crypto_major avg `-0.8249` n `8`; equity avg `0.0598` n `67`; fx avg `0.0458` n `6`; index avg `0.184` n `23`; metal avg `0.4382` n `18`; unknown avg `0.1968` n `418`
- 24h: commodity avg `0.837` n `12`; crypto_alt avg `-2.2117` n `228`; crypto_major avg `-1.606` n `8`; equity avg `-0.5253` n `67`; fx avg `-0.1176` n `6`; index avg `0.3595` n `23`; metal avg `-0.9323` n `18`; unknown avg `0.1` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1741`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1729`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1359`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
