# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T13:07:23.243740+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `-0.0465` n `228`; crypto_major avg `-0.2831` n `8`; equity avg `-0.3041` n `66`; fx avg `0.0227` n `6`; index avg `-0.1682` n `23`; metal avg `-0.6123` n `18`; unknown avg `-0.1374` n `383`
- 1h: commodity avg `-0.0436` n `12`; crypto_alt avg `0.1635` n `228`; crypto_major avg `0.0099` n `8`; equity avg `-0.0996` n `66`; fx avg `0.0004` n `6`; index avg `-0.0349` n `23`; metal avg `-0.4987` n `18`; unknown avg `0.1319` n `383`
- 4h: commodity avg `0.0404` n `12`; crypto_alt avg `-0.673` n `228`; crypto_major avg `-0.631` n `8`; equity avg `-0.7621` n `66`; fx avg `-0.0028` n `6`; index avg `-0.4348` n `23`; metal avg `-0.5048` n `18`; unknown avg `-0.6916` n `383`
- 24h: commodity avg `1.5328` n `12`; crypto_alt avg `0.1095` n `228`; crypto_major avg `-0.4801` n `8`; equity avg `-2.8136` n `66`; fx avg `0.2464` n `6`; index avg `-1.4791` n `23`; metal avg `-1.5674` n `18`; unknown avg `0.2511` n `362`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.2101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
