# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T09:51:06.750208+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0631` n `12`; crypto_alt avg `0.19` n `232`; crypto_major avg `0.0795` n `8`; equity avg `0.0827` n `134`; fx avg `-0.0349` n `6`; index avg `0.0149` n `26`; metal avg `0.0654` n `20`; unknown avg `0.21` n `797`
- 1h: commodity avg `-0.1204` n `12`; crypto_alt avg `0.8209` n `232`; crypto_major avg `0.4946` n `8`; equity avg `0.5264` n `134`; fx avg `-0.0355` n `6`; index avg `0.1076` n `26`; metal avg `0.1072` n `20`; unknown avg `1.0469` n `795`
- 4h: commodity avg `0.068` n `12`; crypto_alt avg `0.6936` n `232`; crypto_major avg `0.4442` n `8`; equity avg `-0.2038` n `134`; fx avg `0.0131` n `6`; index avg `-0.0681` n `26`; metal avg `-0.0831` n `20`; unknown avg `0.8901` n `755`
- 24h: commodity avg `0.4631` n `12`; crypto_alt avg `1.3587` n `232`; crypto_major avg `-0.3312` n `8`; equity avg `-0.156` n `134`; fx avg `-0.0966` n `6`; index avg `-0.0688` n `26`; metal avg `0.0855` n `20`; unknown avg `7463.2072` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
