# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T12:07:44.986384+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `-0.1948` n `234`; crypto_major avg `-0.1641` n `8`; equity avg `-0.0671` n `140`; fx avg `0.0041` n `6`; index avg `-0.0098` n `26`; metal avg `0.08` n `20`; unknown avg `350.682` n `938`
- 1h: commodity avg `0.1318` n `12`; crypto_alt avg `-0.6572` n `234`; crypto_major avg `-0.5916` n `8`; equity avg `-0.3632` n `140`; fx avg `-0.0062` n `6`; index avg `-0.0516` n `26`; metal avg `-0.0189` n `20`; unknown avg `11.26` n `938`
- 4h: commodity avg `0.2301` n `12`; crypto_alt avg `-0.353` n `234`; crypto_major avg `-0.9784` n `8`; equity avg `-0.5395` n `140`; fx avg `-0.0315` n `6`; index avg `-0.0821` n `26`; metal avg `-0.1148` n `20`; unknown avg `10.9612` n `937`
- 24h: commodity avg `0.7676` n `12`; crypto_alt avg `3.0377` n `234`; crypto_major avg `0.0712` n `8`; equity avg `0.4793` n `140`; fx avg `0.0156` n `6`; index avg `0.0057` n `26`; metal avg `-0.1813` n `20`; unknown avg `5.5618` n `842`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1576`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
