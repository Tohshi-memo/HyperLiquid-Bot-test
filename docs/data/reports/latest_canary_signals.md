# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T12:37:34.987185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0848` n `13`; crypto_alt avg `-0.129` n `239`; crypto_major avg `-0.0046` n `8`; equity avg `0.0076` n `166`; fx avg `0.0025` n `6`; index avg `-0.043` n `27`; metal avg `0.0258` n `20`; unknown avg `69.3105` n `1266`
- 1h: commodity avg `-0.0129` n `13`; crypto_alt avg `-0.2148` n `239`; crypto_major avg `-0.3241` n `8`; equity avg `-0.5672` n `166`; fx avg `-0.0187` n `6`; index avg `-0.1157` n `27`; metal avg `-0.0522` n `20`; unknown avg `0.1276` n `1258`
- 4h: commodity avg `-0.1812` n `13`; crypto_alt avg `0.0326` n `239`; crypto_major avg `0.0959` n `8`; equity avg `-0.1629` n `166`; fx avg `-0.0926` n `6`; index avg `-0.0419` n `27`; metal avg `0.0456` n `20`; unknown avg `187.44` n `1198`
- 24h: commodity avg `-0.9781` n `13`; crypto_alt avg `0.9827` n `239`; crypto_major avg `1.5079` n `8`; equity avg `1.6469` n `166`; fx avg `0.1702` n `6`; index avg `0.0516` n `27`; metal avg `0.3656` n `20`; unknown avg `-0.1468` n `1061`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1382`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
