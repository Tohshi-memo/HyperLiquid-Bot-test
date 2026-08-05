# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T20:53:20.178233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `0.0104` n `230`; crypto_major avg `0.0294` n `8`; equity avg `-0.1134` n `108`; fx avg `-0.0035` n `6`; index avg `-0.0196` n `25`; metal avg `-0.0183` n `20`; unknown avg `-0.0027` n `782`
- 1h: commodity avg `0.0148` n `12`; crypto_alt avg `0.1377` n `230`; crypto_major avg `-0.0615` n `8`; equity avg `-0.7264` n `108`; fx avg `-0.0007` n `6`; index avg `-0.08` n `25`; metal avg `-0.0306` n `20`; unknown avg `0.0265` n `782`
- 4h: commodity avg `0.0094` n `12`; crypto_alt avg `0.3148` n `230`; crypto_major avg `0.3524` n `8`; equity avg `-1.1216` n `108`; fx avg `0.0036` n `6`; index avg `-0.1229` n `25`; metal avg `0.0082` n `20`; unknown avg `-0.1698` n `782`
- 24h: commodity avg `-0.0286` n `12`; crypto_alt avg `0.5974` n `230`; crypto_major avg `0.8206` n `8`; equity avg `-0.5951` n `108`; fx avg `-0.049` n `6`; index avg `-0.113` n `25`; metal avg `0.7784` n `20`; unknown avg `0.7253` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
