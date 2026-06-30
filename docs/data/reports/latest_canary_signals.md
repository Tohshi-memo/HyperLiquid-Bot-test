# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T05:52:30.957035+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `0.1785` n `228`; crypto_major avg `0.2049` n `8`; equity avg `0.1264` n `88`; fx avg `0.0017` n `6`; index avg `0.0296` n `23`; metal avg `-0.0287` n `20`; unknown avg `-0.1303` n `765`
- 1h: commodity avg `-0.0185` n `12`; crypto_alt avg `-0.1517` n `228`; crypto_major avg `-0.0149` n `8`; equity avg `-0.1268` n `88`; fx avg `-0.0112` n `6`; index avg `-0.0317` n `23`; metal avg `-0.1777` n `20`; unknown avg `-0.8243` n `763`
- 4h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.0018` n `228`; crypto_major avg `-0.2256` n `8`; equity avg `0.5511` n `88`; fx avg `-0.0466` n `6`; index avg `0.1695` n `23`; metal avg `0.1239` n `20`; unknown avg `8.6477` n `761`
- 24h: commodity avg `-0.1546` n `12`; crypto_alt avg `0.0239` n `228`; crypto_major avg `1.091` n `8`; equity avg `2.0917` n `88`; fx avg `0.152` n `6`; index avg `0.243` n `23`; metal avg `-0.6199` n `20`; unknown avg `11.029` n `726`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
