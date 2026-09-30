# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T02:29:19.596238+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `-0.6114` n `234`; crypto_major avg `-0.3183` n `8`; equity avg `-0.2255` n `142`; fx avg `-0.0552` n `6`; index avg `-0.0226` n `26`; metal avg `0.0012` n `20`; unknown avg `2.9604` n `963`
- 1h: commodity avg `-0.0909` n `12`; crypto_alt avg `-0.439` n `234`; crypto_major avg `-0.0526` n `8`; equity avg `-0.2011` n `142`; fx avg `-0.0767` n `6`; index avg `-0.0258` n `26`; metal avg `-0.0057` n `20`; unknown avg `7.4746` n `961`
- 4h: commodity avg `0.1094` n `12`; crypto_alt avg `-0.0787` n `234`; crypto_major avg `-0.1002` n `8`; equity avg `-0.285` n `142`; fx avg `-0.0784` n `6`; index avg `-0.0696` n `26`; metal avg `-0.1181` n `20`; unknown avg `6.8583` n `954`
- 24h: commodity avg `-0.9241` n `12`; crypto_alt avg `2.6949` n `234`; crypto_major avg `1.0005` n `8`; equity avg `0.8106` n `142`; fx avg `-0.2263` n `6`; index avg `0.0926` n `26`; metal avg `0.1777` n `20`; unknown avg `3258.0489` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1803`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
