# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T13:22:30.617403+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0764` n `12`; crypto_alt avg `0.0386` n `234`; crypto_major avg `0.1679` n `8`; equity avg `0.2121` n `140`; fx avg `-0.0042` n `6`; index avg `0.0102` n `26`; metal avg `-0.0434` n `20`; unknown avg `0.9126` n `946`
- 1h: commodity avg `-0.1331` n `12`; crypto_alt avg `-0.3572` n `234`; crypto_major avg `-0.1876` n `8`; equity avg `0.3141` n `140`; fx avg `-0.0009` n `6`; index avg `0.0243` n `26`; metal avg `-0.1056` n `20`; unknown avg `89.0233` n `944`
- 4h: commodity avg `0.0966` n `12`; crypto_alt avg `-1.3437` n `234`; crypto_major avg `-1.0185` n `8`; equity avg `-0.2738` n `140`; fx avg `0.0039` n `6`; index avg `-0.0657` n `26`; metal avg `-0.2413` n `20`; unknown avg `4.2076` n `937`
- 24h: commodity avg `0.6767` n `12`; crypto_alt avg `1.5526` n `234`; crypto_major avg `-0.5552` n `8`; equity avg `0.8399` n `140`; fx avg `-0.027` n `6`; index avg `0.0089` n `26`; metal avg `-0.5167` n `20`; unknown avg `2.4346` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
