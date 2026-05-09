# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T17:37:18.254294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.07` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0081` n `12`; crypto_alt avg `0.2358` n `228`; crypto_major avg `0.1892` n `8`; equity avg `0.0071` n `65`; fx avg `0.0` n `5`; index avg `-0.0001` n `23`; metal avg `-0.0063` n `18`; unknown avg `0.1125` n `376`
- 1h: commodity avg `-0.0104` n `12`; crypto_alt avg `0.7093` n `228`; crypto_major avg `0.366` n `8`; equity avg `0.0895` n `65`; fx avg `0.0` n `5`; index avg `0.0045` n `23`; metal avg `0.015` n `18`; unknown avg `0.4425` n `376`
- 4h: commodity avg `0.3284` n `12`; crypto_alt avg `0.421` n `228`; crypto_major avg `0.1672` n `8`; equity avg `0.0885` n `65`; fx avg `-0.0011` n `5`; index avg `0.0319` n `23`; metal avg `-0.0217` n `18`; unknown avg `0.0219` n `376`
- 24h: commodity avg `-0.0314` n `12`; crypto_alt avg `1.1132` n `228`; crypto_major avg `0.9271` n `8`; equity avg `1.4455` n `65`; fx avg `0.0007` n `5`; index avg `0.3427` n `23`; metal avg `-0.1265` n `18`; unknown avg `0.0956` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
