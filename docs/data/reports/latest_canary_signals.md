# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T21:07:26.299728+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0368` n `13`; crypto_alt avg `-0.3414` n `239`; crypto_major avg `-0.1641` n `8`; equity avg `-0.2782` n `162`; fx avg `-0.0141` n `6`; index avg `-0.0174` n `27`; metal avg `-0.0477` n `20`; unknown avg `-0.4353` n `1230`
- 1h: commodity avg `-0.035` n `13`; crypto_alt avg `-0.6202` n `239`; crypto_major avg `-0.3896` n `8`; equity avg `-0.4674` n `162`; fx avg `-0.0166` n `6`; index avg `-0.0639` n `27`; metal avg `-0.1198` n `20`; unknown avg `1.332` n `1230`
- 4h: commodity avg `-0.2321` n `13`; crypto_alt avg `-0.3902` n `239`; crypto_major avg `0.0221` n `8`; equity avg `-1.0555` n `162`; fx avg `-0.0379` n `6`; index avg `-0.1605` n `27`; metal avg `-0.1947` n `20`; unknown avg `6.5435` n `1219`
- 24h: commodity avg `-1.136` n `13`; crypto_alt avg `-0.478` n `239`; crypto_major avg `-0.0823` n `8`; equity avg `-3.4386` n `162`; fx avg `-0.1489` n `6`; index avg `-0.3547` n `27`; metal avg `-0.4225` n `20`; unknown avg `479.4191` n `1027`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
