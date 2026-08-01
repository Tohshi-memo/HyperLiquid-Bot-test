# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T20:52:31.438123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0279` n `12`; crypto_alt avg `-0.0057` n `230`; crypto_major avg `0.0127` n `8`; equity avg `0.0025` n `102`; fx avg `0.0194` n `6`; index avg `-0.0089` n `25`; metal avg `-0.0099` n `20`; unknown avg `-0.1025` n `782`
- 1h: commodity avg `-0.0318` n `12`; crypto_alt avg `-0.1287` n `230`; crypto_major avg `0.0585` n `8`; equity avg `-0.0199` n `102`; fx avg `-0.0047` n `6`; index avg `-0.008` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.1456` n `782`
- 4h: commodity avg `0.0127` n `12`; crypto_alt avg `-1.0821` n `230`; crypto_major avg `-1.0395` n `8`; equity avg `-0.2633` n `102`; fx avg `-0.015` n `6`; index avg `-0.0462` n `25`; metal avg `-0.0166` n `20`; unknown avg `2.8559` n `782`
- 24h: commodity avg `0.5601` n `12`; crypto_alt avg `-0.8061` n `230`; crypto_major avg `-1.232` n `8`; equity avg `-0.7529` n `102`; fx avg `-0.0505` n `6`; index avg `-0.0969` n `25`; metal avg `-0.0624` n `20`; unknown avg `4.3128` n `765`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
