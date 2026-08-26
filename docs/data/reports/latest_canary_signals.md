# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T03:15:24.200684+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0108` n `12`; crypto_alt avg `-0.069` n `231`; crypto_major avg `-0.0271` n `8`; equity avg `-0.0211` n `122`; fx avg `0.0047` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0253` n `20`; unknown avg `-0.0966` n `797`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `0.115` n `231`; crypto_major avg `0.0695` n `8`; equity avg `0.2403` n `122`; fx avg `0.065` n `6`; index avg `0.0711` n `25`; metal avg `-0.0617` n `20`; unknown avg `0.2264` n `797`
- 4h: commodity avg `-0.1293` n `12`; crypto_alt avg `0.9311` n `231`; crypto_major avg `0.5262` n `8`; equity avg `-0.0675` n `122`; fx avg `0.0162` n `6`; index avg `0.0251` n `25`; metal avg `0.0581` n `20`; unknown avg `0.6442` n `795`
- 24h: commodity avg `-0.8733` n `12`; crypto_alt avg `-2.6952` n `231`; crypto_major avg `-2.8075` n `8`; equity avg `1.5299` n `122`; fx avg `0.0414` n `6`; index avg `0.2085` n `25`; metal avg `0.2971` n `20`; unknown avg `0.0892` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
