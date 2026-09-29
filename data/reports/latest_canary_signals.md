# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T02:07:31.718526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0311` n `12`; crypto_alt avg `-0.1837` n `234`; crypto_major avg `0.0238` n `8`; equity avg `-0.1938` n `141`; fx avg `-0.0019` n `6`; index avg `-0.023` n `26`; metal avg `-0.026` n `20`; unknown avg `-0.1643` n `961`
- 1h: commodity avg `0.0301` n `12`; crypto_alt avg `-1.1888` n `234`; crypto_major avg `-0.4551` n `8`; equity avg `-0.1165` n `141`; fx avg `0.0245` n `6`; index avg `0.0004` n `26`; metal avg `0.0055` n `20`; unknown avg `0.2556` n `961`
- 4h: commodity avg `0.0312` n `12`; crypto_alt avg `-0.4644` n `234`; crypto_major avg `-0.2076` n `8`; equity avg `-0.3632` n `141`; fx avg `-0.0224` n `6`; index avg `-0.0553` n `26`; metal avg `-0.0697` n `20`; unknown avg `-0.085` n `955`
- 24h: commodity avg `0.015` n `12`; crypto_alt avg `-3.9102` n `234`; crypto_major avg `-1.7257` n `8`; equity avg `-2.3195` n `141`; fx avg `-0.0855` n `6`; index avg `-0.1925` n `26`; metal avg `-0.5815` n `20`; unknown avg `164.1247` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
