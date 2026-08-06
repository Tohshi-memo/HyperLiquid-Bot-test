# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T04:52:34.877691+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.0549` n `230`; crypto_major avg `-0.0944` n `8`; equity avg `-0.0108` n `108`; fx avg `-0.0053` n `6`; index avg `0.0027` n `25`; metal avg `0.0073` n `20`; unknown avg `0.0071` n `782`
- 1h: commodity avg `-0.075` n `12`; crypto_alt avg `0.2246` n `230`; crypto_major avg `0.2338` n `8`; equity avg `0.0914` n `108`; fx avg `0.0002` n `6`; index avg `0.0167` n `25`; metal avg `0.003` n `20`; unknown avg `0.0871` n `782`
- 4h: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.1668` n `230`; crypto_major avg `-0.4607` n `8`; equity avg `0.2825` n `108`; fx avg `0.012` n `6`; index avg `-0.0114` n `25`; metal avg `-0.1466` n `20`; unknown avg `-0.0358` n `782`
- 24h: commodity avg `-0.0968` n `12`; crypto_alt avg `0.1652` n `230`; crypto_major avg `0.0849` n `8`; equity avg `-1.9081` n `108`; fx avg `-0.046` n `6`; index avg `-0.3456` n `25`; metal avg `0.5231` n `20`; unknown avg `0.9418` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1837`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
