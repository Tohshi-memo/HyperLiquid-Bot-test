# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T08:52:18.832570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1218` n `12`; crypto_alt avg `-0.0069` n `228`; crypto_major avg `0.1008` n `8`; equity avg `0.0956` n `66`; fx avg `-0.0046` n `6`; index avg `0.023` n `23`; metal avg `-0.0419` n `18`; unknown avg `0.0125` n `383`
- 1h: commodity avg `-0.0478` n `12`; crypto_alt avg `-0.3612` n `228`; crypto_major avg `-0.1874` n `8`; equity avg `-0.3436` n `66`; fx avg `-0.0166` n `6`; index avg `-0.2215` n `23`; metal avg `-0.2525` n `18`; unknown avg `0.0262` n `383`
- 4h: commodity avg `0.1637` n `12`; crypto_alt avg `-0.1317` n `228`; crypto_major avg `0.0697` n `8`; equity avg `0.2969` n `66`; fx avg `-0.01` n `6`; index avg `0.1356` n `23`; metal avg `-0.122` n `18`; unknown avg `0.1211` n `363`
- 24h: commodity avg `0.609` n `12`; crypto_alt avg `1.6367` n `228`; crypto_major avg `0.9858` n `8`; equity avg `-1.4191` n `66`; fx avg `0.3021` n `6`; index avg `-0.6559` n `23`; metal avg `-0.3572` n `18`; unknown avg `0.7339` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
