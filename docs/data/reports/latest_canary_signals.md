# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T08:56:23.791957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `12`; crypto_alt avg `-0.0563` n `230`; crypto_major avg `-0.0039` n `8`; equity avg `0.0244` n `92`; fx avg `0.0068` n `6`; index avg `0.0024` n `25`; metal avg `-0.0001` n `20`; unknown avg `4.3271` n `765`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `0.1732` n `230`; crypto_major avg `0.2438` n `8`; equity avg `0.0696` n `92`; fx avg `0.0047` n `6`; index avg `0.025` n `25`; metal avg `-0.0035` n `20`; unknown avg `6.2713` n `765`
- 4h: commodity avg `0.0709` n `12`; crypto_alt avg `-0.2086` n `230`; crypto_major avg `-0.0239` n `8`; equity avg `-0.1014` n `92`; fx avg `0.0088` n `6`; index avg `0.0024` n `25`; metal avg `-0.0279` n `20`; unknown avg `2.0286` n `747`
- 24h: commodity avg `0.5033` n `12`; crypto_alt avg `-0.7079` n `230`; crypto_major avg `-0.6297` n `8`; equity avg `-0.1397` n `92`; fx avg `0.0024` n `6`; index avg `-0.1027` n `25`; metal avg `-0.1111` n `20`; unknown avg `0.0412` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
