# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T13:37:41.968694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1566` n `13`; crypto_alt avg `-0.1916` n `235`; crypto_major avg `-0.1966` n `8`; equity avg `-0.2346` n `150`; fx avg `0.0078` n `6`; index avg `-0.0666` n `26`; metal avg `-0.1289` n `20`; unknown avg `10.1529` n `1076`
- 1h: commodity avg `0.1123` n `13`; crypto_alt avg `-0.6886` n `235`; crypto_major avg `-0.64` n `8`; equity avg `-0.2932` n `150`; fx avg `0.0264` n `6`; index avg `-0.092` n `26`; metal avg `0.0163` n `20`; unknown avg `15.4518` n `1074`
- 4h: commodity avg `0.3123` n `13`; crypto_alt avg `-1.3139` n `235`; crypto_major avg `-1.061` n `8`; equity avg `-0.7993` n `150`; fx avg `-0.0173` n `6`; index avg `-0.2065` n `26`; metal avg `-0.3102` n `20`; unknown avg `5.4148` n `1068`
- 24h: commodity avg `1.384` n `13`; crypto_alt avg `-5.8142` n `235`; crypto_major avg `-4.2445` n `8`; equity avg `-2.0986` n `150`; fx avg `-0.1486` n `6`; index avg `-0.4344` n `26`; metal avg `-0.7657` n `20`; unknown avg `814.6321` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0715`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
