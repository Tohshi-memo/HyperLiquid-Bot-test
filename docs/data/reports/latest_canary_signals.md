# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T04:52:38.646615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0579` n `12`; crypto_alt avg `0.0157` n `234`; crypto_major avg `-0.0513` n `8`; equity avg `-0.0375` n `140`; fx avg `0.0058` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0205` n `20`; unknown avg `0.039` n `945`
- 1h: commodity avg `-0.0485` n `12`; crypto_alt avg `-0.1424` n `234`; crypto_major avg `0.4171` n `8`; equity avg `0.1708` n `140`; fx avg `-0.0395` n `6`; index avg `0.0206` n `26`; metal avg `0.0178` n `20`; unknown avg `0.2368` n `937`
- 4h: commodity avg `-0.201` n `12`; crypto_alt avg `0.9502` n `234`; crypto_major avg `1.1407` n `8`; equity avg `-0.072` n `140`; fx avg `-0.0323` n `6`; index avg `-0.0089` n `26`; metal avg `-0.2077` n `20`; unknown avg `-0.2044` n `937`
- 24h: commodity avg `-0.2475` n `12`; crypto_alt avg `4.1753` n `234`; crypto_major avg `2.8951` n `8`; equity avg `1.1513` n `140`; fx avg `-0.2047` n `6`; index avg `0.1013` n `26`; metal avg `0.157` n `20`; unknown avg `1.8597` n `836`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1494`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
