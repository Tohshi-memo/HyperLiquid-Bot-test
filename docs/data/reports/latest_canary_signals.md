# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T20:52:21.205620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1162` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0982` n `12`; crypto_alt avg `0.1258` n `228`; crypto_major avg `0.0021` n `8`; equity avg `0.0163` n `67`; fx avg `-0.0047` n `6`; index avg `-0.0612` n `23`; metal avg `-0.0257` n `18`; unknown avg `-0.1836` n `418`
- 1h: commodity avg `-0.0451` n `12`; crypto_alt avg `-0.0673` n `228`; crypto_major avg `-0.3737` n `8`; equity avg `0.0102` n `67`; fx avg `0.0068` n `6`; index avg `-0.1024` n `23`; metal avg `0.034` n `18`; unknown avg `-0.1528` n `418`
- 4h: commodity avg `-0.4611` n `12`; crypto_alt avg `-1.0159` n `228`; crypto_major avg `-0.9844` n `8`; equity avg `0.0372` n `67`; fx avg `0.0266` n `6`; index avg `0.1318` n `23`; metal avg `0.4273` n `18`; unknown avg `-0.5587` n `418`
- 24h: commodity avg `0.6878` n `12`; crypto_alt avg `-1.7661` n `228`; crypto_major avg `-1.4475` n `8`; equity avg `-0.4165` n `67`; fx avg `-0.0885` n `6`; index avg `0.4174` n `23`; metal avg `-0.8896` n `18`; unknown avg `0.1982` n `395`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1731`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
