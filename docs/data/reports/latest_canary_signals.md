# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T00:22:34.882515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `13`; crypto_alt avg `0.2983` n `234`; crypto_major avg `0.113` n `8`; equity avg `0.2285` n `142`; fx avg `0.0316` n `6`; index avg `0.0534` n `26`; metal avg `-0.031` n `20`; unknown avg `0.0417` n `985`
- 1h: commodity avg `0.0054` n `13`; crypto_alt avg `0.5314` n `234`; crypto_major avg `0.2196` n `8`; equity avg `0.179` n `142`; fx avg `0.059` n `6`; index avg `0.037` n `26`; metal avg `-0.0473` n `20`; unknown avg `-0.0554` n `977`
- 4h: commodity avg `-0.0004` n `13`; crypto_alt avg `0.0682` n `234`; crypto_major avg `-0.0073` n `8`; equity avg `0.2478` n `142`; fx avg `0.0554` n `6`; index avg `0.0446` n `26`; metal avg `-0.0156` n `20`; unknown avg `-0.2538` n `935`
- 24h: commodity avg `0.0339` n `13`; crypto_alt avg `-0.0449` n `234`; crypto_major avg `0.1147` n `8`; equity avg `1.2469` n `142`; fx avg `-0.105` n `6`; index avg `0.221` n `26`; metal avg `0.0911` n `20`; unknown avg `0.0935` n `824`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
