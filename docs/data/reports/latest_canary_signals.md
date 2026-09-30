# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T14:07:35.071426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.32` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.0449` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.1121` n `234`; crypto_major avg `-0.1086` n `8`; equity avg `0.2577` n `142`; fx avg `0.0032` n `6`; index avg `0.0918` n `26`; metal avg `0.0744` n `20`; unknown avg `1.6306` n `929`
- 1h: commodity avg `0.0315` n `12`; crypto_alt avg `-0.6941` n `234`; crypto_major avg `-1.0293` n `8`; equity avg `-0.3317` n `142`; fx avg `0.0165` n `6`; index avg `0.0156` n `26`; metal avg `-0.1156` n `20`; unknown avg `17.5103` n `929`
- 4h: commodity avg `0.0299` n `12`; crypto_alt avg `0.7355` n `234`; crypto_major avg `0.5501` n `8`; equity avg `0.2809` n `142`; fx avg `-0.0192` n `6`; index avg `0.1527` n `26`; metal avg `-0.0206` n `20`; unknown avg `5.6702` n `923`
- 24h: commodity avg `-0.086` n `12`; crypto_alt avg `0.3861` n `234`; crypto_major avg `-0.2051` n `8`; equity avg `0.142` n `142`; fx avg `0.0153` n `6`; index avg `0.1902` n `26`; metal avg `0.1332` n `20`; unknown avg `240.1993` n `816`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
