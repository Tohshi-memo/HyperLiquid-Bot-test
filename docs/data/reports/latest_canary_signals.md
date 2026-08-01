# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T16:52:31.719695+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.1857` n `230`; crypto_major avg `-0.0982` n `8`; equity avg `-0.0176` n `102`; fx avg `0.0046` n `6`; index avg `0.0009` n `25`; metal avg `0.0005` n `20`; unknown avg `-0.0509` n `782`
- 1h: commodity avg `0.071` n `12`; crypto_alt avg `0.0636` n `230`; crypto_major avg `-0.002` n `8`; equity avg `-0.049` n `102`; fx avg `0.0227` n `6`; index avg `-0.023` n `25`; metal avg `-0.0057` n `20`; unknown avg `-0.0753` n `782`
- 4h: commodity avg `0.0429` n `12`; crypto_alt avg `-0.0689` n `230`; crypto_major avg `-0.0258` n `8`; equity avg `-0.16` n `102`; fx avg `0.005` n `6`; index avg `0.0034` n `25`; metal avg `0.0068` n `20`; unknown avg `-0.1673` n `782`
- 24h: commodity avg `0.668` n `12`; crypto_alt avg `0.1745` n `230`; crypto_major avg `-0.4084` n `8`; equity avg `-0.7372` n `102`; fx avg `-0.0954` n `6`; index avg `-0.0689` n `25`; metal avg `0.0907` n `20`; unknown avg `4.2947` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
