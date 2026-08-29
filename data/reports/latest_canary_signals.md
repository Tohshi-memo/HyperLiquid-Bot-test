# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T02:37:31.986945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.33` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.0255` n `231`; crypto_major avg `-0.0048` n `8`; equity avg `0.02` n `127`; fx avg `0.0018` n `6`; index avg `0.0087` n `26`; metal avg `-0.0033` n `20`; unknown avg `-0.0076` n `793`
- 1h: commodity avg `-0.01` n `12`; crypto_alt avg `-0.2172` n `231`; crypto_major avg `-0.1957` n `8`; equity avg `0.0449` n `127`; fx avg `-0.0035` n `6`; index avg `0.0171` n `26`; metal avg `0.0252` n `20`; unknown avg `2.7816` n `793`
- 4h: commodity avg `-0.0439` n `12`; crypto_alt avg `0.1521` n `231`; crypto_major avg `-0.0432` n `8`; equity avg `0.1024` n `127`; fx avg `-0.0094` n `6`; index avg `0.0215` n `26`; metal avg `0.0181` n `20`; unknown avg `1.2631` n `793`
- 24h: commodity avg `-0.1066` n `12`; crypto_alt avg `-2.0913` n `231`; crypto_major avg `-2.9205` n `8`; equity avg `-2.0384` n `127`; fx avg `-0.1158` n `6`; index avg `-0.2186` n `26`; metal avg `-0.2323` n `20`; unknown avg `-0.4756` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
