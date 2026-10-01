# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T06:07:29.413362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.056` n `13`; crypto_alt avg `0.0152` n `234`; crypto_major avg `-0.0469` n `8`; equity avg `0.092` n `142`; fx avg `-0.0031` n `6`; index avg `0.0218` n `26`; metal avg `0.0472` n `20`; unknown avg `-0.0361` n `946`
- 1h: commodity avg `0.3815` n `13`; crypto_alt avg `0.0705` n `234`; crypto_major avg `0.1404` n `8`; equity avg `0.2195` n `142`; fx avg `0.0317` n `6`; index avg `0.0409` n `26`; metal avg `0.0703` n `20`; unknown avg `0.4664` n `946`
- 4h: commodity avg `-0.1144` n `13`; crypto_alt avg `1.2041` n `234`; crypto_major avg `0.6802` n `8`; equity avg `1.069` n `142`; fx avg `-0.0087` n `6`; index avg `0.234` n `26`; metal avg `0.3018` n `20`; unknown avg `1.2022` n `940`
- 24h: commodity avg `-0.2342` n `13`; crypto_alt avg `1.1806` n `234`; crypto_major avg `1.2772` n `8`; equity avg `1.1673` n `142`; fx avg `0.1492` n `6`; index avg `0.3142` n `26`; metal avg `0.0829` n `20`; unknown avg `773.8186` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
