# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T04:37:28.759865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6483` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.5923` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0015` n `13`; crypto_alt avg `0.4867` n `234`; crypto_major avg `0.3933` n `8`; equity avg `0.0593` n `142`; fx avg `-0.0089` n `6`; index avg `0.0018` n `26`; metal avg `-0.0112` n `20`; unknown avg `-0.3117` n `985`
- 1h: commodity avg `-0.0356` n `13`; crypto_alt avg `1.0873` n `234`; crypto_major avg `1.1614` n `8`; equity avg `0.1169` n `142`; fx avg `-0.0112` n `6`; index avg `0.0112` n `26`; metal avg `0.0814` n `20`; unknown avg `0.771` n `977`
- 4h: commodity avg `-0.1742` n `13`; crypto_alt avg `1.3429` n `234`; crypto_major avg `1.7544` n `8`; equity avg `0.1061` n `142`; fx avg `-0.0786` n `6`; index avg `0.0348` n `26`; metal avg `0.1621` n `20`; unknown avg `2.5226` n `977`
- 24h: commodity avg `0.623` n `13`; crypto_alt avg `0.2662` n `234`; crypto_major avg `1.564` n `8`; equity avg `0.484` n `142`; fx avg `-0.2218` n `6`; index avg `0.0218` n `26`; metal avg `-0.063` n `20`; unknown avg `1.0296` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
