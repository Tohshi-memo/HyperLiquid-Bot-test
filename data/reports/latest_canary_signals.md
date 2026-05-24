# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T09:07:15.724123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0066` n `12`; crypto_alt avg `0.1151` n `228`; crypto_major avg `0.0709` n `8`; equity avg `-0.0043` n `67`; fx avg `-0.0055` n `6`; index avg `0.0123` n `23`; metal avg `-0.0051` n `18`; unknown avg `0.1112` n `396`
- 1h: commodity avg `0.0741` n `12`; crypto_alt avg `0.4105` n `228`; crypto_major avg `0.4691` n `8`; equity avg `0.0541` n `67`; fx avg `0.0019` n `6`; index avg `0.0354` n `23`; metal avg `-0.015` n `18`; unknown avg `1.3635` n `396`
- 4h: commodity avg `0.2363` n `12`; crypto_alt avg `0.3206` n `228`; crypto_major avg `0.7056` n `8`; equity avg `0.0285` n `67`; fx avg `-0.0206` n `6`; index avg `0.0313` n `23`; metal avg `0.078` n `18`; unknown avg `1.328` n `386`
- 24h: commodity avg `-2.7146` n `12`; crypto_alt avg `4.0762` n `228`; crypto_major avg `4.4539` n `8`; equity avg `2.6768` n `67`; fx avg `0.0678` n `6`; index avg `1.3897` n `23`; metal avg `1.2915` n `18`; unknown avg `2.3517` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
