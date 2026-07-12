# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T08:52:25.173137+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0237` n `12`; crypto_alt avg `-0.0292` n `230`; crypto_major avg `-0.0052` n `8`; equity avg `0.008` n `92`; fx avg `0.0068` n `6`; index avg `0.0014` n `25`; metal avg `-0.0005` n `20`; unknown avg `4.2169` n `765`
- 1h: commodity avg `-0.0145` n `12`; crypto_alt avg `0.2007` n `230`; crypto_major avg `0.2425` n `8`; equity avg `0.0531` n `92`; fx avg `0.0047` n `6`; index avg `0.024` n `25`; metal avg `-0.0039` n `20`; unknown avg `5.26` n `765`
- 4h: commodity avg `0.0665` n `12`; crypto_alt avg `-0.1819` n `230`; crypto_major avg `-0.0252` n `8`; equity avg `-0.1179` n `92`; fx avg `0.0088` n `6`; index avg `0.0014` n `25`; metal avg `-0.0283` n `20`; unknown avg `1.9682` n `747`
- 24h: commodity avg `0.4988` n `12`; crypto_alt avg `-0.6808` n `230`; crypto_major avg `-0.6311` n `8`; equity avg `-0.1561` n `92`; fx avg `0.0024` n `6`; index avg `-0.1036` n `25`; metal avg `-0.1114` n `20`; unknown avg `0.062` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1394`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
