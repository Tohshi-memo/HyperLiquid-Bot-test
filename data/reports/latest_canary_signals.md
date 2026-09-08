# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T03:37:29.208006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0468` n `12`; crypto_alt avg `0.2803` n `232`; crypto_major avg `0.2786` n `8`; equity avg `0.1555` n `134`; fx avg `-0.005` n `6`; index avg `0.0222` n `26`; metal avg `-0.0208` n `20`; unknown avg `1.8045` n `797`
- 1h: commodity avg `0.0815` n `12`; crypto_alt avg `-0.354` n `232`; crypto_major avg `-0.328` n `8`; equity avg `0.0648` n `134`; fx avg `0.022` n `6`; index avg `0.0252` n `26`; metal avg `0.0677` n `20`; unknown avg `0.4556` n `795`
- 4h: commodity avg `-0.0174` n `12`; crypto_alt avg `0.292` n `232`; crypto_major avg `-0.2101` n `8`; equity avg `0.6703` n `134`; fx avg `-0.1471` n `6`; index avg `0.1837` n `26`; metal avg `0.1018` n `20`; unknown avg `5.6737` n `783`
- 24h: commodity avg `0.1877` n `12`; crypto_alt avg `0.8179` n `232`; crypto_major avg `-0.8077` n `8`; equity avg `0.8253` n `134`; fx avg `-0.3239` n `6`; index avg `0.2271` n `26`; metal avg `0.3195` n `20`; unknown avg `7374.5923` n `678`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
