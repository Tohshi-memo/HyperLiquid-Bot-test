# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T21:07:28.435025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0243` n `12`; crypto_alt avg `-0.0466` n `233`; crypto_major avg `0.0789` n `8`; equity avg `-0.0233` n `134`; fx avg `-0.0045` n `6`; index avg `0.005` n `26`; metal avg `0.0205` n `20`; unknown avg `121.5515` n `781`
- 1h: commodity avg `0.0058` n `12`; crypto_alt avg `0.04` n `233`; crypto_major avg `0.0872` n `8`; equity avg `0.0079` n `134`; fx avg `-0.0074` n `6`; index avg `0.0164` n `26`; metal avg `0.0386` n `20`; unknown avg `5.5535` n `765`
- 4h: commodity avg `0.178` n `12`; crypto_alt avg `-1.3896` n `233`; crypto_major avg `-0.9604` n `8`; equity avg `-0.3288` n `134`; fx avg `-0.0085` n `6`; index avg `0.0023` n `26`; metal avg `-0.2285` n `20`; unknown avg `3.1971` n `745`
- 24h: commodity avg `0.1235` n `12`; crypto_alt avg `-1.5487` n `233`; crypto_major avg `-0.9722` n `8`; equity avg `-0.4053` n `134`; fx avg `-0.0359` n `6`; index avg `-0.1221` n `26`; metal avg `0.509` n `20`; unknown avg `152.0191` n `699`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
