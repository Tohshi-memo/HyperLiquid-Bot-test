# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T08:37:29.323905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0469` n `13`; crypto_alt avg `-0.0311` n `235`; crypto_major avg `0.0019` n `8`; equity avg `-0.0523` n `150`; fx avg `0.015` n `6`; index avg `-0.0144` n `26`; metal avg `-0.0023` n `20`; unknown avg `0.3917` n `1076`
- 1h: commodity avg `-0.0454` n `13`; crypto_alt avg `-0.2895` n `235`; crypto_major avg `-0.1224` n `8`; equity avg `-0.133` n `150`; fx avg `-0.0326` n `6`; index avg `-0.0127` n `26`; metal avg `-0.0185` n `20`; unknown avg `0.2865` n `1058`
- 4h: commodity avg `0.0097` n `13`; crypto_alt avg `0.5894` n `235`; crypto_major avg `0.5137` n `8`; equity avg `-0.3317` n `150`; fx avg `-0.0984` n `6`; index avg `-0.0661` n `26`; metal avg `-0.1502` n `20`; unknown avg `0.5466` n `1036`
- 24h: commodity avg `0.8648` n `13`; crypto_alt avg `-3.5251` n `235`; crypto_major avg `-2.1709` n `8`; equity avg `-0.443` n `149`; fx avg `-0.0686` n `6`; index avg `-0.132` n `26`; metal avg `-0.3095` n `20`; unknown avg `815.2133` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1692`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
