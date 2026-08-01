# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T23:37:30.928863+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0336` n `12`; crypto_alt avg `0.0185` n `230`; crypto_major avg `0.0222` n `8`; equity avg `0.0031` n `102`; fx avg `-0.0299` n `6`; index avg `-0.0029` n `25`; metal avg `-0.0015` n `20`; unknown avg `0.0255` n `782`
- 1h: commodity avg `0.007` n `12`; crypto_alt avg `-0.123` n `230`; crypto_major avg `-0.0514` n `8`; equity avg `0.0115` n `102`; fx avg `-0.0775` n `6`; index avg `0.0138` n `25`; metal avg `-0.0103` n `20`; unknown avg `1.8196` n `782`
- 4h: commodity avg `-0.202` n `12`; crypto_alt avg `0.2879` n `230`; crypto_major avg `0.5252` n `8`; equity avg `0.299` n `102`; fx avg `-0.0508` n `6`; index avg `0.0148` n `25`; metal avg `0.0311` n `20`; unknown avg `0.1716` n `782`
- 24h: commodity avg `-0.1663` n `12`; crypto_alt avg `-0.571` n `230`; crypto_major avg `-0.8086` n `8`; equity avg `-0.0994` n `102`; fx avg `-0.1027` n `6`; index avg `-0.0024` n `25`; metal avg `0.0414` n `20`; unknown avg `-0.001` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
