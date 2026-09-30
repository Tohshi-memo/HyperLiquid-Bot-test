# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T20:22:46.525434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.5295` n `234`; crypto_major avg `0.3911` n `8`; equity avg `0.2162` n `142`; fx avg `0.0127` n `6`; index avg `0.0361` n `26`; metal avg `0.0228` n `20`; unknown avg `0.2184` n `951`
- 1h: commodity avg `0.0254` n `12`; crypto_alt avg `0.4461` n `234`; crypto_major avg `0.2196` n `8`; equity avg `-0.0572` n `142`; fx avg `0.021` n `6`; index avg `-0.0489` n `26`; metal avg `-0.0183` n `20`; unknown avg `15.7415` n `929`
- 4h: commodity avg `-0.1321` n `12`; crypto_alt avg `-1.044` n `234`; crypto_major avg `-0.4138` n `8`; equity avg `-0.1631` n `142`; fx avg `0.017` n `6`; index avg `-0.1222` n `26`; metal avg `0.015` n `20`; unknown avg `7.7838` n `929`
- 24h: commodity avg `0.3521` n `12`; crypto_alt avg `0.251` n `234`; crypto_major avg `0.7016` n `8`; equity avg `-0.2231` n `142`; fx avg `0.0811` n `6`; index avg `-0.028` n `26`; metal avg `-0.2015` n `20`; unknown avg `7.5047` n `790`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
