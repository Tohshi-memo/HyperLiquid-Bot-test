# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T05:22:30.797543+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `0.3196` n `234`; crypto_major avg `0.3054` n `8`; equity avg `0.0613` n `141`; fx avg `-0.025` n `6`; index avg `0.0068` n `26`; metal avg `0.0246` n `20`; unknown avg `0.5438` n `963`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `-0.0579` n `234`; crypto_major avg `-0.0298` n `8`; equity avg `-0.0257` n `141`; fx avg `-0.0104` n `6`; index avg `-0.0112` n `26`; metal avg `0.013` n `20`; unknown avg `-0.0095` n `961`
- 4h: commodity avg `0.1036` n `12`; crypto_alt avg `0.1534` n `234`; crypto_major avg `0.386` n `8`; equity avg `-0.0444` n `141`; fx avg `-0.0445` n `6`; index avg `-0.0491` n `26`; metal avg `-0.0256` n `20`; unknown avg `0.4928` n `955`
- 24h: commodity avg `0.0482` n `12`; crypto_alt avg `-1.6266` n `234`; crypto_major avg `-0.4691` n `8`; equity avg `-2.0472` n `141`; fx avg `-0.1145` n `6`; index avg `-0.2387` n `26`; metal avg `-0.4213` n `20`; unknown avg `10.125` n `810`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1771`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
