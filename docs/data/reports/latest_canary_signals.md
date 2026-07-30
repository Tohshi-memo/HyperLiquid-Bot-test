# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T12:01:49.405470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0309` n `12`; crypto_alt avg `0.0145` n `230`; crypto_major avg `-0.009` n `8`; equity avg `-0.0005` n `102`; fx avg `0.0107` n `6`; index avg `-0.0007` n `25`; metal avg `-0.0453` n `20`; unknown avg `0.0113` n `779`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `0.2969` n `230`; crypto_major avg `0.2032` n `8`; equity avg `0.4069` n `102`; fx avg `0.0225` n `6`; index avg `0.0713` n `25`; metal avg `-0.0285` n `20`; unknown avg `-0.0101` n `779`
- 4h: commodity avg `-0.2195` n `12`; crypto_alt avg `0.3421` n `230`; crypto_major avg `0.764` n `8`; equity avg `2.0736` n `102`; fx avg `-0.0344` n `6`; index avg `0.3406` n `25`; metal avg `0.2857` n `20`; unknown avg `0.0715` n `771`
- 24h: commodity avg `0.3552` n `12`; crypto_alt avg `0.1118` n `230`; crypto_major avg `0.2123` n `8`; equity avg `-1.7248` n `102`; fx avg `-0.0403` n `6`; index avg `-0.2508` n `25`; metal avg `0.4252` n `20`; unknown avg `-0.15` n `737`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
