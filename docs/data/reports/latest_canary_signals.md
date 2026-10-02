# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T08:23:03.831282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0739` n `13`; crypto_alt avg `0.2928` n `234`; crypto_major avg `0.4126` n `8`; equity avg `0.1088` n `142`; fx avg `0.0061` n `6`; index avg `0.0056` n `26`; metal avg `-0.0332` n `20`; unknown avg `0.1699` n `973`
- 1h: commodity avg `-0.3198` n `13`; crypto_alt avg `0.7141` n `234`; crypto_major avg `0.8288` n `8`; equity avg `0.4464` n `142`; fx avg `-0.0614` n `6`; index avg `0.077` n `26`; metal avg `0.0393` n `20`; unknown avg `-0.1344` n `907`
- 4h: commodity avg `-0.488` n `13`; crypto_alt avg `1.1267` n `234`; crypto_major avg `0.9312` n `8`; equity avg `0.5545` n `142`; fx avg `-0.1361` n `6`; index avg `0.1112` n `26`; metal avg `0.0362` n `20`; unknown avg `0.8694` n `891`
- 24h: commodity avg `-0.6575` n `13`; crypto_alt avg `1.9035` n `234`; crypto_major avg `2.7326` n `8`; equity avg `1.4635` n `142`; fx avg `-0.3356` n `6`; index avg `0.3042` n `26`; metal avg `0.3176` n `20`; unknown avg `1.2388` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1698`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
