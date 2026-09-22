# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T20:22:32.887341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0498` n `12`; crypto_alt avg `0.0951` n `234`; crypto_major avg `-0.044` n `8`; equity avg `-0.0378` n `140`; fx avg `-0.0133` n `6`; index avg `-0.0108` n `26`; metal avg `-0.0135` n `20`; unknown avg `5.3458` n `914`
- 1h: commodity avg `-0.0278` n `12`; crypto_alt avg `-0.1297` n `234`; crypto_major avg `-0.425` n `8`; equity avg `-0.0043` n `140`; fx avg `-0.0419` n `6`; index avg `-0.0009` n `26`; metal avg `0.0103` n `20`; unknown avg `5.0931` n `906`
- 4h: commodity avg `-0.0695` n `12`; crypto_alt avg `1.3649` n `234`; crypto_major avg `0.7774` n `8`; equity avg `0.5062` n `140`; fx avg `-0.0297` n `6`; index avg `0.0824` n `26`; metal avg `0.3758` n `20`; unknown avg `3.8052` n `866`
- 24h: commodity avg `0.19` n `12`; crypto_alt avg `1.7207` n `234`; crypto_major avg `-0.0316` n `8`; equity avg `0.8852` n `140`; fx avg `-0.3023` n `6`; index avg `0.1276` n `26`; metal avg `0.2987` n `20`; unknown avg `1.1816` n `832`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
