# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T02:07:31.650999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0206` n `13`; crypto_alt avg `0.0139` n `235`; crypto_major avg `-0.1261` n `8`; equity avg `0.005` n `143`; fx avg `-0.0038` n `6`; index avg `0.0085` n `26`; metal avg `0.0061` n `20`; unknown avg `-0.058` n `982`
- 1h: commodity avg `-0.1372` n `13`; crypto_alt avg `-0.2549` n `235`; crypto_major avg `-0.1251` n `8`; equity avg `0.0313` n `143`; fx avg `-0.0019` n `6`; index avg `0.0232` n `26`; metal avg `-0.0038` n `20`; unknown avg `-0.1634` n `982`
- 4h: commodity avg `-0.1811` n `13`; crypto_alt avg `1.1081` n `235`; crypto_major avg `0.7877` n `8`; equity avg `0.099` n `143`; fx avg `0.0123` n `6`; index avg `0.0985` n `26`; metal avg `-0.0205` n `20`; unknown avg `0.8006` n `976`
- 24h: commodity avg `0.0537` n `13`; crypto_alt avg `-0.6778` n `235`; crypto_major avg `-0.5807` n `8`; equity avg `0.7355` n `142`; fx avg `-0.1237` n `6`; index avg `0.2881` n `26`; metal avg `-0.0786` n `20`; unknown avg `-0.7174` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
