# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T09:37:18.541482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.86` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.023` n `12`; crypto_alt avg `0.1689` n `228`; crypto_major avg `0.1336` n `8`; equity avg `-0.0481` n `67`; fx avg `-0.0012` n `6`; index avg `0.0162` n `23`; metal avg `-0.0104` n `18`; unknown avg `-0.7364` n `396`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `0.2386` n `228`; crypto_major avg `0.3112` n `8`; equity avg `0.0262` n `67`; fx avg `0.0006` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0399` n `18`; unknown avg `-0.9656` n `396`
- 4h: commodity avg `0.2126` n `12`; crypto_alt avg `0.7515` n `228`; crypto_major avg `1.1396` n `8`; equity avg `0.072` n `67`; fx avg `0.0162` n `6`; index avg `0.0062` n `23`; metal avg `0.0419` n `18`; unknown avg `-0.3853` n `386`
- 24h: commodity avg `-2.7719` n `12`; crypto_alt avg `4.1599` n `228`; crypto_major avg `4.8103` n `8`; equity avg `2.5504` n `67`; fx avg `0.0717` n `6`; index avg `1.3621` n `23`; metal avg `1.2557` n `18`; unknown avg `1.3747` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
