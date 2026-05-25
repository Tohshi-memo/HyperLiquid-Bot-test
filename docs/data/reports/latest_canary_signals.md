# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T07:37:14.143698+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1176` n `12`; crypto_alt avg `0.0563` n `228`; crypto_major avg `0.1123` n `8`; equity avg `0.0709` n `67`; fx avg `-0.0023` n `6`; index avg `0.0817` n `23`; metal avg `0.231` n `18`; unknown avg `-0.0614` n `397`
- 1h: commodity avg `0.2165` n `12`; crypto_alt avg `-0.0547` n `228`; crypto_major avg `-0.072` n `8`; equity avg `0.081` n `67`; fx avg `0.0189` n `6`; index avg `0.0316` n `23`; metal avg `0.1914` n `18`; unknown avg `-0.2856` n `397`
- 4h: commodity avg `0.575` n `12`; crypto_alt avg `1.0084` n `228`; crypto_major avg `0.7489` n `8`; equity avg `0.1386` n `67`; fx avg `0.0557` n `6`; index avg `0.3363` n `23`; metal avg `-0.0001` n `18`; unknown avg `0.2157` n `387`
- 24h: commodity avg `0.253` n `12`; crypto_alt avg `0.0229` n `228`; crypto_major avg `0.1407` n `8`; equity avg `0.4606` n `67`; fx avg `-0.0101` n `6`; index avg `-0.1021` n `23`; metal avg `0.4897` n `18`; unknown avg `-0.1319` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
