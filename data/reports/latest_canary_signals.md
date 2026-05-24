# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T09:45:32.781018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.86` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0708` n `12`; crypto_alt avg `-0.0645` n `228`; crypto_major avg `0.0418` n `8`; equity avg `0.1325` n `67`; fx avg `0.0` n `6`; index avg `0.0166` n `23`; metal avg `0.0118` n `18`; unknown avg `0.0195` n `396`
- 1h: commodity avg `0.043` n `12`; crypto_alt avg `0.2366` n `228`; crypto_major avg `0.3966` n `8`; equity avg `0.0905` n `67`; fx avg `-0.0016` n `6`; index avg `0.0261` n `23`; metal avg `-0.0209` n `18`; unknown avg `-0.9954` n `396`
- 4h: commodity avg `0.2822` n `12`; crypto_alt avg `0.5194` n `228`; crypto_major avg `0.8044` n `8`; equity avg `0.0838` n `67`; fx avg `0.0048` n `6`; index avg `0.0205` n `23`; metal avg `0.0152` n `18`; unknown avg `-0.4742` n `386`
- 24h: commodity avg `-2.7152` n `12`; crypto_alt avg `4.1214` n `228`; crypto_major avg `4.8591` n `8`; equity avg `2.6907` n `67`; fx avg `0.0717` n `6`; index avg `1.3729` n `23`; metal avg `1.2859` n `18`; unknown avg `1.2632` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
