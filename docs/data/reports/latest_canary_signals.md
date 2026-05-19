# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T12:22:17.587939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0796` n `12`; crypto_alt avg `0.0918` n `228`; crypto_major avg `0.0052` n `8`; equity avg `0.0109` n `66`; fx avg `-0.0065` n `6`; index avg `0.0023` n `23`; metal avg `0.1182` n `18`; unknown avg `0.0104` n `383`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `-0.06` n `228`; crypto_major avg `-0.1655` n `8`; equity avg `-0.1933` n `66`; fx avg `0.0024` n `6`; index avg `-0.1123` n `23`; metal avg `-0.1032` n `18`; unknown avg `-0.0508` n `383`
- 4h: commodity avg `0.1931` n `12`; crypto_alt avg `-0.8531` n `228`; crypto_major avg `-0.6258` n `8`; equity avg `-0.8542` n `66`; fx avg `-0.0713` n `6`; index avg `-0.4424` n `23`; metal avg `-0.1912` n `18`; unknown avg `-0.6397` n `383`
- 24h: commodity avg `0.8964` n `12`; crypto_alt avg `-0.1044` n `228`; crypto_major avg `-0.4113` n `8`; equity avg `-2.0748` n `66`; fx avg `0.2049` n `6`; index avg `-0.9175` n `23`; metal avg `-0.5933` n `18`; unknown avg `0.2719` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
