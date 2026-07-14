# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T18:44:59.902255+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1186` n `12`; crypto_alt avg `-0.021` n `230`; crypto_major avg `0.1855` n `8`; equity avg `-0.118` n `92`; fx avg `-0.002` n `6`; index avg `-0.0235` n `25`; metal avg `-0.0837` n `20`; unknown avg `-0.0787` n `768`
- 1h: commodity avg `0.1517` n `12`; crypto_alt avg `-0.1297` n `230`; crypto_major avg `0.297` n `8`; equity avg `0.0507` n `92`; fx avg `-0.0032` n `6`; index avg `-0.0069` n `25`; metal avg `-0.098` n `20`; unknown avg `-0.1914` n `767`
- 4h: commodity avg `0.1055` n `12`; crypto_alt avg `-0.2051` n `230`; crypto_major avg `0.5124` n `8`; equity avg `0.3317` n `92`; fx avg `-0.031` n `6`; index avg `0.0748` n `25`; metal avg `-0.2463` n `20`; unknown avg `-0.3208` n `758`
- 24h: commodity avg `0.3174` n `12`; crypto_alt avg `1.7956` n `230`; crypto_major avg `3.5785` n `8`; equity avg `1.2864` n `92`; fx avg `-0.0218` n `6`; index avg `0.3598` n `25`; metal avg `0.5294` n `20`; unknown avg `-0.0562` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
