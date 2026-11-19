# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T05:52:33.842860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.02` n `13`; crypto_alt avg `-0.0786` n `239`; crypto_major avg `-0.0524` n `8`; equity avg `-0.0998` n `164`; fx avg `0.0122` n `6`; index avg `-0.0057` n `27`; metal avg `0.0137` n `20`; unknown avg `5461.6184` n `1266`
- 1h: commodity avg `0.0562` n `13`; crypto_alt avg `-0.3593` n `239`; crypto_major avg `-0.0915` n `8`; equity avg `0.0228` n `164`; fx avg `0.004` n `6`; index avg `0.019` n `27`; metal avg `0.1753` n `20`; unknown avg `5520.1312` n `1262`
- 4h: commodity avg `-0.0989` n `13`; crypto_alt avg `0.5764` n `239`; crypto_major avg `1.1294` n `8`; equity avg `0.3519` n `164`; fx avg `-0.0086` n `6`; index avg `0.0962` n `27`; metal avg `-0.0274` n `20`; unknown avg `5836.415` n `1239`
- 24h: commodity avg `0.1667` n `13`; crypto_alt avg `-0.2573` n `239`; crypto_major avg `-1.0436` n `8`; equity avg `-0.666` n `164`; fx avg `-0.1064` n `6`; index avg `0.046` n `27`; metal avg `-0.4361` n `20`; unknown avg `7557.2576` n `1115`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
