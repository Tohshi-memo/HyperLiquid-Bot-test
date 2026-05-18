# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T07:52:16.368297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1692` n `12`; crypto_alt avg `-0.1129` n `228`; crypto_major avg `0.01` n `8`; equity avg `-0.063` n `66`; fx avg `0.0089` n `5`; index avg `-0.0314` n `23`; metal avg `-0.2229` n `18`; unknown avg `-0.2018` n `383`
- 1h: commodity avg `-0.278` n `12`; crypto_alt avg `-0.3759` n `228`; crypto_major avg `-0.1257` n `8`; equity avg `0.1861` n `66`; fx avg `-0.018` n `5`; index avg `0.0103` n `23`; metal avg `0.074` n `18`; unknown avg `-0.343` n `383`
- 4h: commodity avg `-0.2181` n `12`; crypto_alt avg `-0.6916` n `228`; crypto_major avg `-0.4178` n `8`; equity avg `0.2205` n `66`; fx avg `-0.0586` n `5`; index avg `0.0689` n `23`; metal avg `0.4522` n `18`; unknown avg `-0.2678` n `363`
- 24h: commodity avg `0.6919` n `12`; crypto_alt avg `-3.1796` n `228`; crypto_major avg `-1.4048` n `8`; equity avg `0.0436` n `65`; fx avg `0.0436` n `5`; index avg `0.099` n `23`; metal avg `-0.092` n `18`; unknown avg `-0.3803` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
