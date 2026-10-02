# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T08:07:29.252921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3096` n `13`; crypto_alt avg `0.1891` n `234`; crypto_major avg `0.3375` n `8`; equity avg `0.2325` n `142`; fx avg `-0.0167` n `6`; index avg `0.0463` n `26`; metal avg `0.0633` n `20`; unknown avg `-0.2932` n `913`
- 1h: commodity avg `-0.4231` n `13`; crypto_alt avg `0.3838` n `234`; crypto_major avg `0.2543` n `8`; equity avg `0.3631` n `142`; fx avg `-0.0622` n `6`; index avg `0.079` n `26`; metal avg `0.1217` n `20`; unknown avg `0.383` n `913`
- 4h: commodity avg `-0.5613` n `13`; crypto_alt avg `1.2771` n `234`; crypto_major avg `0.9644` n `8`; equity avg `0.4863` n `142`; fx avg `-0.1433` n `6`; index avg `0.1061` n `26`; metal avg `0.0926` n `20`; unknown avg `1.4015` n `897`
- 24h: commodity avg `-0.7457` n `13`; crypto_alt avg `1.5957` n `234`; crypto_major avg `2.2868` n `8`; equity avg `1.1682` n `142`; fx avg `-0.3671` n `6`; index avg `0.2477` n `26`; metal avg `0.2228` n `20`; unknown avg `613.5327` n `801`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1656`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
