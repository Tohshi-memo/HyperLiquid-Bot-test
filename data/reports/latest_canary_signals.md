# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T03:52:26.924842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0249` n `12`; crypto_alt avg `0.2729` n `234`; crypto_major avg `0.1069` n `8`; equity avg `0.1704` n `140`; fx avg `0.0041` n `6`; index avg `0.0069` n `26`; metal avg `0.0344` n `20`; unknown avg `1.2712` n `945`
- 1h: commodity avg `-0.0974` n `12`; crypto_alt avg `0.9448` n `234`; crypto_major avg `0.6329` n `8`; equity avg `0.0631` n `140`; fx avg `-0.0072` n `6`; index avg `0.02` n `26`; metal avg `0.0485` n `20`; unknown avg `-0.0729` n `943`
- 4h: commodity avg `-0.0827` n `12`; crypto_alt avg `0.9969` n `234`; crypto_major avg `1.0739` n `8`; equity avg `-0.3593` n `140`; fx avg `-0.0009` n `6`; index avg `-0.0954` n `26`; metal avg `-0.2417` n `20`; unknown avg `-0.1034` n `937`
- 24h: commodity avg `-0.1086` n `12`; crypto_alt avg `4.1974` n `234`; crypto_major avg `2.5467` n `8`; equity avg `0.4083` n `140`; fx avg `-0.1761` n `6`; index avg `0.0177` n `26`; metal avg `0.1393` n `20`; unknown avg `0.9348` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
