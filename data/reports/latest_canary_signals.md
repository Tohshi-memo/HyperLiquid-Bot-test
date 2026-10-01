# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T19:07:33.332888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `13`; crypto_alt avg `0.147` n `234`; crypto_major avg `0.1699` n `8`; equity avg `-0.0108` n `142`; fx avg `-0.0091` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0024` n `20`; unknown avg `4.519` n `973`
- 1h: commodity avg `-0.1037` n `13`; crypto_alt avg `0.0897` n `234`; crypto_major avg `0.175` n `8`; equity avg `0.3355` n `142`; fx avg `-0.0103` n `6`; index avg `0.0772` n `26`; metal avg `0.082` n `20`; unknown avg `0.1994` n `973`
- 4h: commodity avg `0.0021` n `13`; crypto_alt avg `1.2517` n `234`; crypto_major avg `0.6734` n `8`; equity avg `1.2306` n `142`; fx avg `-0.0628` n `6`; index avg `0.2442` n `26`; metal avg `0.1437` n `20`; unknown avg `1.9569` n `957`
- 24h: commodity avg `-0.0257` n `13`; crypto_alt avg `0.0757` n `234`; crypto_major avg `0.168` n `8`; equity avg `0.8386` n `142`; fx avg `-0.0929` n `6`; index avg `0.1379` n `26`; metal avg `-0.0383` n `20`; unknown avg `-0.019` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1792`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
