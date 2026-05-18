# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T05:52:13.801024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0492` n `12`; crypto_alt avg `-0.122` n `228`; crypto_major avg `-0.2243` n `8`; equity avg `-0.0024` n `66`; fx avg `0.0026` n `5`; index avg `0.0151` n `23`; metal avg `-0.2073` n `18`; unknown avg `-0.4043` n `383`
- 1h: commodity avg `-0.169` n `12`; crypto_alt avg `-0.3625` n `228`; crypto_major avg `-0.3007` n `8`; equity avg `0.1401` n `66`; fx avg `-0.0224` n `5`; index avg `0.1037` n `23`; metal avg `-0.0747` n `18`; unknown avg `1.9441` n `383`
- 4h: commodity avg `-0.1217` n `12`; crypto_alt avg `0.2359` n `228`; crypto_major avg `-0.114` n `8`; equity avg `0.2108` n `66`; fx avg `-0.0007` n `5`; index avg `0.2316` n `23`; metal avg `-0.0591` n `18`; unknown avg `0.0752` n `383`
- 24h: commodity avg `2.5449` n `12`; crypto_alt avg `-11.0451` n `228`; crypto_major avg `-3.4939` n `8`; equity avg `-3.0046` n `65`; fx avg `-0.085` n `5`; index avg `-1.6704` n `23`; metal avg `-6.2111` n `18`; unknown avg `549.9296` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
