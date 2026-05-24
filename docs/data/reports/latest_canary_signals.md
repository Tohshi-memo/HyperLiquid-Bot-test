# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T07:52:14.392932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0819` n `12`; crypto_alt avg `-0.0853` n `228`; crypto_major avg `0.0161` n `8`; equity avg `-0.0034` n `67`; fx avg `0.0` n `6`; index avg `0.0021` n `23`; metal avg `0.0629` n `18`; unknown avg `-0.1097` n `396`
- 1h: commodity avg `0.1866` n `12`; crypto_alt avg `-0.2529` n `228`; crypto_major avg `-0.1796` n `8`; equity avg `0.0248` n `67`; fx avg `-0.005` n `6`; index avg `0.0421` n `23`; metal avg `0.0507` n `18`; unknown avg `0.0113` n `396`
- 4h: commodity avg `0.0512` n `12`; crypto_alt avg `-0.0106` n `228`; crypto_major avg `0.3498` n `8`; equity avg `0.1546` n `67`; fx avg `0.0112` n `6`; index avg `0.0623` n `23`; metal avg `0.0507` n `18`; unknown avg `-0.199` n `386`
- 24h: commodity avg `-2.7896` n `12`; crypto_alt avg `4.2235` n `228`; crypto_major avg `4.4469` n `8`; equity avg `2.4794` n `67`; fx avg `0.0389` n `6`; index avg `1.4255` n `23`; metal avg `1.3005` n `18`; unknown avg `2.3559` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
