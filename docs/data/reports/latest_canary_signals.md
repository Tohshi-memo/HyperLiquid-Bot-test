# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T05:07:38.004650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0186` n `12`; crypto_alt avg `-0.0686` n `234`; crypto_major avg `-0.0887` n `8`; equity avg `-0.0414` n `141`; fx avg `0.0135` n `6`; index avg `-0.009` n `26`; metal avg `-0.0097` n `20`; unknown avg `0.416` n `961`
- 1h: commodity avg `0.0037` n `12`; crypto_alt avg `0.4289` n `234`; crypto_major avg `0.0887` n `8`; equity avg `-0.0273` n `141`; fx avg `0.0051` n `6`; index avg `-0.0127` n `26`; metal avg `-0.005` n `20`; unknown avg `11.9408` n `961`
- 4h: commodity avg `0.1235` n `12`; crypto_alt avg `-0.6586` n `234`; crypto_major avg `-0.1298` n `8`; equity avg `-0.2765` n `141`; fx avg `0.001` n `6`; index avg `-0.0742` n `26`; metal avg `-0.0447` n `20`; unknown avg `0.9953` n `955`
- 24h: commodity avg `0.0686` n `12`; crypto_alt avg `-2.3997` n `234`; crypto_major avg `-1.1032` n `8`; equity avg `-2.2821` n `141`; fx avg `-0.0701` n `6`; index avg `-0.2739` n `26`; metal avg `-0.5` n `20`; unknown avg `10.2435` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
