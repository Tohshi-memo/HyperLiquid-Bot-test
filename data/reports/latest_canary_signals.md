# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T04:37:26.270851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `13`; crypto_alt avg `-0.4447` n `239`; crypto_major avg `-0.1691` n `8`; equity avg `0.0428` n `168`; fx avg `0.0094` n `6`; index avg `-0.0025` n `27`; metal avg `0.0033` n `20`; unknown avg `0.6533` n `1263`
- 1h: commodity avg `-0.0082` n `13`; crypto_alt avg `-0.326` n `239`; crypto_major avg `-0.099` n `8`; equity avg `0.0694` n `168`; fx avg `0.008` n `6`; index avg `-0.001` n `27`; metal avg `0.003` n `20`; unknown avg `0.9729` n `1241`
- 4h: commodity avg `0.1305` n `13`; crypto_alt avg `-0.8661` n `239`; crypto_major avg `-0.0298` n `8`; equity avg `0.2565` n `168`; fx avg `0.0146` n `6`; index avg `0.0095` n `27`; metal avg `0.0172` n `20`; unknown avg `30.556` n `1241`
- 24h: commodity avg `-0.8028` n `13`; crypto_alt avg `-1.899` n `239`; crypto_major avg `-1.8448` n `8`; equity avg `0.6597` n `168`; fx avg `-0.1217` n `6`; index avg `0.0421` n `27`; metal avg `0.1073` n `20`; unknown avg `214.4025` n `979`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
