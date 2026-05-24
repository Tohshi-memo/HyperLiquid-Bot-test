# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T09:22:13.007097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `71.5` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `0.0156` n `228`; crypto_major avg `0.1484` n `8`; equity avg `0.017` n `67`; fx avg `0.0052` n `6`; index avg `-0.0188` n `23`; metal avg `-0.0172` n `18`; unknown avg `-0.375` n `396`
- 1h: commodity avg `0.1046` n `12`; crypto_alt avg `0.2179` n `228`; crypto_major avg `0.4674` n `8`; equity avg `0.0155` n `67`; fx avg `0.0058` n `6`; index avg `-0.0015` n `23`; metal avg `-0.0475` n `18`; unknown avg `-0.1379` n `396`
- 4h: commodity avg `0.2487` n `12`; crypto_alt avg `0.5335` n `228`; crypto_major avg `0.9515` n `8`; equity avg `0.074` n `67`; fx avg `0.0039` n `6`; index avg `0.0161` n `23`; metal avg `0.0685` n `18`; unknown avg `1.1623` n `386`
- 24h: commodity avg `-2.7678` n `12`; crypto_alt avg `4.1038` n `228`; crypto_major avg `4.6373` n `8`; equity avg `2.6618` n `67`; fx avg `0.0729` n `6`; index avg `1.3642` n `23`; metal avg `1.2742` n `18`; unknown avg `1.9483` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
