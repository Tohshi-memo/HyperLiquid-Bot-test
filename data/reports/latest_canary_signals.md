# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T09:37:29.850834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0211` n `12`; crypto_alt avg `0.5301` n `232`; crypto_major avg `0.4646` n `8`; equity avg `0.236` n `134`; fx avg `0.0` n `6`; index avg `0.0378` n `26`; metal avg `0.0149` n `20`; unknown avg `0.0568` n `797`
- 1h: commodity avg `-0.0214` n `12`; crypto_alt avg `0.5687` n `232`; crypto_major avg `0.3036` n `8`; equity avg `0.4153` n `134`; fx avg `0.0125` n `6`; index avg `0.0868` n `26`; metal avg `0.0166` n `20`; unknown avg `1.0996` n `795`
- 4h: commodity avg `0.2118` n `12`; crypto_alt avg `0.4362` n `232`; crypto_major avg `0.289` n `8`; equity avg `-0.4694` n `134`; fx avg `0.0499` n `6`; index avg `-0.1321` n `26`; metal avg `-0.158` n `20`; unknown avg `0.5174` n `755`
- 24h: commodity avg `0.5206` n `12`; crypto_alt avg `1.0539` n `232`; crypto_major avg `-0.4891` n `8`; equity avg `-0.2442` n `134`; fx avg `-0.0585` n `6`; index avg `-0.0836` n `26`; metal avg `0.0173` n `20`; unknown avg `7462.4939` n `670`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
