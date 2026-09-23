# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T06:07:32.142381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.045` n `12`; crypto_alt avg `0.3361` n `234`; crypto_major avg `0.0283` n `8`; equity avg `0.0162` n `140`; fx avg `-0.0045` n `6`; index avg `0.0066` n `26`; metal avg `-0.0035` n `20`; unknown avg `0.145` n `927`
- 1h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.0195` n `234`; crypto_major avg `-0.4848` n `8`; equity avg `-0.0192` n `140`; fx avg `0.0372` n `6`; index avg `0.0137` n `26`; metal avg `-0.0972` n `20`; unknown avg `0.3869` n `927`
- 4h: commodity avg `-0.0843` n `12`; crypto_alt avg `1.4683` n `234`; crypto_major avg `0.7433` n `8`; equity avg `0.1878` n `140`; fx avg `0.0009` n `6`; index avg `0.0413` n `26`; metal avg `-0.044` n `20`; unknown avg `-0.1253` n `921`
- 24h: commodity avg `-0.2419` n `12`; crypto_alt avg `4.2046` n `234`; crypto_major avg `2.1479` n `8`; equity avg `1.2873` n `140`; fx avg `-0.1642` n `6`; index avg `0.1302` n `26`; metal avg `0.2109` n `20`; unknown avg `2.607` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1569`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
