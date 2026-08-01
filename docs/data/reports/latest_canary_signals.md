# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T21:52:28.392658+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `12`; crypto_alt avg `0.0276` n `230`; crypto_major avg `0.0843` n `8`; equity avg `0.2135` n `102`; fx avg `0.0003` n `6`; index avg `0.0148` n `25`; metal avg `-0.0115` n `20`; unknown avg `-0.0476` n `782`
- 1h: commodity avg `-0.1026` n `12`; crypto_alt avg `0.4254` n `230`; crypto_major avg `0.3843` n `8`; equity avg `0.4043` n `102`; fx avg `0.0248` n `6`; index avg `0.0507` n `25`; metal avg `0.0667` n `20`; unknown avg `0.4078` n `782`
- 4h: commodity avg `-0.1236` n `12`; crypto_alt avg `-0.1025` n `230`; crypto_major avg `-0.0761` n `8`; equity avg `0.2131` n `102`; fx avg `0.0215` n `6`; index avg `0.0246` n `25`; metal avg `0.07` n `20`; unknown avg `0.0141` n `782`
- 24h: commodity avg `-0.2752` n `12`; crypto_alt avg `-0.2974` n `230`; crypto_major avg `-0.7594` n `8`; equity avg `-0.0512` n `102`; fx avg `-0.037` n `6`; index avg `0.0263` n `25`; metal avg `0.0491` n `20`; unknown avg `3.021` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
