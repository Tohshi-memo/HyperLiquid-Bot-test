# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T16:07:38.150741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1449` n `13`; crypto_alt avg `0.1921` n `234`; crypto_major avg `0.0602` n `8`; equity avg `0.2466` n `142`; fx avg `0.0202` n `6`; index avg `0.0624` n `26`; metal avg `0.0948` n `20`; unknown avg `0.7686` n `967`
- 1h: commodity avg `-0.1122` n `13`; crypto_alt avg `0.6918` n `234`; crypto_major avg `0.1053` n `8`; equity avg `0.3596` n `142`; fx avg `-0.0459` n `6`; index avg `0.0614` n `26`; metal avg `0.0995` n `20`; unknown avg `0.7115` n `957`
- 4h: commodity avg `0.0921` n `13`; crypto_alt avg `-0.5042` n `234`; crypto_major avg `-0.6956` n `8`; equity avg `-0.42` n `142`; fx avg `-0.15` n `6`; index avg `-0.1974` n `26`; metal avg `-0.198` n `20`; unknown avg `1.3193` n `909`
- 24h: commodity avg `-0.2744` n `13`; crypto_alt avg `-1.6924` n `234`; crypto_major avg `-0.7199` n `8`; equity avg `-0.0665` n `142`; fx avg `-0.0842` n `6`; index avg `-0.1309` n `26`; metal avg `-0.0564` n `20`; unknown avg `0.2526` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
