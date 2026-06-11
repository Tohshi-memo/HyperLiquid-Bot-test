# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T09:07:32.560150+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0765` n `12`; crypto_alt avg `-0.114` n `228`; crypto_major avg `-0.1264` n `8`; equity avg `-0.0439` n `74`; fx avg `0.0107` n `6`; index avg `0.0427` n `23`; metal avg `-0.2343` n `18`; unknown avg `4.1251` n `556`
- 1h: commodity avg `-0.1612` n `12`; crypto_alt avg `0.1838` n `228`; crypto_major avg `0.1874` n `8`; equity avg `0.1566` n `74`; fx avg `-0.0188` n `6`; index avg `0.0615` n `23`; metal avg `-0.5431` n `18`; unknown avg `4.1903` n `556`
- 4h: commodity avg `-0.788` n `12`; crypto_alt avg `0.1235` n `228`; crypto_major avg `0.6442` n `8`; equity avg `0.8565` n `74`; fx avg `0.021` n `6`; index avg `0.4115` n `23`; metal avg `0.1276` n `18`; unknown avg `4.345` n `530`
- 24h: commodity avg `0.8241` n `12`; crypto_alt avg `1.5871` n `228`; crypto_major avg `1.6666` n `8`; equity avg `1.1233` n `74`; fx avg `0.0095` n `6`; index avg `0.2029` n `23`; metal avg `-0.436` n `18`; unknown avg `8.1603` n `527`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
