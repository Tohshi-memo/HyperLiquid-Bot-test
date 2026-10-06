# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T17:07:36.540262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `13`; crypto_alt avg `-0.2306` n `235`; crypto_major avg `-0.1373` n `8`; equity avg `-0.0683` n `150`; fx avg `0.008` n `6`; index avg `-0.0186` n `26`; metal avg `0.0401` n `20`; unknown avg `0.0958` n `1074`
- 1h: commodity avg `0.1148` n `13`; crypto_alt avg `-0.4132` n `235`; crypto_major avg `-0.3604` n `8`; equity avg `-0.0636` n `150`; fx avg `0.0041` n `6`; index avg `-0.0378` n `26`; metal avg `-0.0204` n `20`; unknown avg `0.7672` n `1074`
- 4h: commodity avg `0.4411` n `13`; crypto_alt avg `-0.6116` n `235`; crypto_major avg `-0.4552` n `8`; equity avg `-0.028` n `150`; fx avg `-0.0089` n `6`; index avg `-0.0791` n `26`; metal avg `0.0326` n `20`; unknown avg `6.0578` n `1018`
- 24h: commodity avg `-0.0873` n `13`; crypto_alt avg `0.268` n `235`; crypto_major avg `0.0642` n `8`; equity avg `0.7904` n `149`; fx avg `0.128` n `6`; index avg `0.0769` n `26`; metal avg `0.079` n `20`; unknown avg `381.6249` n `912`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
