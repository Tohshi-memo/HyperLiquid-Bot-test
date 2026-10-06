# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T20:52:32.457838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `13`; crypto_alt avg `-0.0508` n `235`; crypto_major avg `-0.0074` n `8`; equity avg `0.0302` n `150`; fx avg `-0.0019` n `6`; index avg `0.0107` n `26`; metal avg `-0.006` n `20`; unknown avg `1.9112` n `1076`
- 1h: commodity avg `0.0778` n `13`; crypto_alt avg `0.0936` n `235`; crypto_major avg `0.1093` n `8`; equity avg `0.1523` n `150`; fx avg `-0.0025` n `6`; index avg `0.0259` n `26`; metal avg `-0.0196` n `20`; unknown avg `9.8783` n `1012`
- 4h: commodity avg `0.4254` n `13`; crypto_alt avg `-0.4626` n `235`; crypto_major avg `-0.238` n `8`; equity avg `-0.1758` n `150`; fx avg `-0.0003` n `6`; index avg `-0.0649` n `26`; metal avg `0.0605` n `20`; unknown avg `7.1775` n `1012`
- 24h: commodity avg `0.3465` n `13`; crypto_alt avg `-1.0498` n `235`; crypto_major avg `-0.6748` n `8`; equity avg `0.4166` n `149`; fx avg `0.0982` n `6`; index avg `-0.0093` n `26`; metal avg `0.04` n `20`; unknown avg `867.5288` n `922`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
