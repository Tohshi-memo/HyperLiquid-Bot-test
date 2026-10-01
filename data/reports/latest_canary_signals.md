# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T15:07:33.120201+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `13`; crypto_alt avg `0.1988` n `234`; crypto_major avg `0.1543` n `8`; equity avg `-0.1403` n `142`; fx avg `0.0141` n `6`; index avg `-0.0376` n `26`; metal avg `-0.0658` n `20`; unknown avg `0.0844` n `971`
- 1h: commodity avg `0.1092` n `13`; crypto_alt avg `-0.3199` n `234`; crypto_major avg `-0.2402` n `8`; equity avg `0.1105` n `142`; fx avg `-0.0828` n `6`; index avg `-0.0328` n `26`; metal avg `-0.0924` n `20`; unknown avg `0.0867` n `917`
- 4h: commodity avg `0.1692` n `13`; crypto_alt avg `-0.9286` n `234`; crypto_major avg `-0.5222` n `8`; equity avg `-0.9274` n `142`; fx avg `-0.1156` n `6`; index avg `-0.2555` n `26`; metal avg `-0.1785` n `20`; unknown avg `0.9554` n `911`
- 24h: commodity avg `-0.1654` n `13`; crypto_alt avg `-1.5717` n `234`; crypto_major avg `0.0061` n `8`; equity avg `-0.393` n `142`; fx avg `-0.0591` n `6`; index avg `-0.1771` n `26`; metal avg `-0.1563` n `20`; unknown avg `3.3015` n `832`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
