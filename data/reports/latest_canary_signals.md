# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T20:52:30.014345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0291` n `12`; crypto_alt avg `0.0397` n `232`; crypto_major avg `0.0632` n `8`; equity avg `0.0318` n `134`; fx avg `0.002` n `6`; index avg `-0.0024` n `26`; metal avg `0.0025` n `20`; unknown avg `0.3721` n `796`
- 1h: commodity avg `-0.0299` n `12`; crypto_alt avg `-0.0104` n `232`; crypto_major avg `-0.0879` n `8`; equity avg `-0.0047` n `134`; fx avg `0.0044` n `6`; index avg `0.0003` n `26`; metal avg `0.0099` n `20`; unknown avg `7.5835` n `756`
- 4h: commodity avg `-0.0076` n `12`; crypto_alt avg `0.3561` n `232`; crypto_major avg `0.287` n `8`; equity avg `0.2289` n `134`; fx avg `-0.0092` n `6`; index avg `0.0419` n `26`; metal avg `0.0165` n `20`; unknown avg `0.0107` n `738`
- 24h: commodity avg `0.16` n `12`; crypto_alt avg `0.3423` n `232`; crypto_major avg `-1.0076` n `8`; equity avg `0.4816` n `134`; fx avg `-0.128` n `6`; index avg `0.0814` n `26`; metal avg `0.0034` n `20`; unknown avg `7801.2882` n `641`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
