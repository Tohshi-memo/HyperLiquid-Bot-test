# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T23:22:38.380184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `13`; crypto_alt avg `-0.0786` n `239`; crypto_major avg `-0.0477` n `8`; equity avg `-0.0734` n `162`; fx avg `-0.0056` n `6`; index avg `-0.0087` n `27`; metal avg `-0.0168` n `20`; unknown avg `158.0774` n `1264`
- 1h: commodity avg `0.0129` n `13`; crypto_alt avg `-0.3485` n `239`; crypto_major avg `-0.2478` n `8`; equity avg `-0.2103` n `162`; fx avg `-0.0084` n `6`; index avg `-0.0087` n `27`; metal avg `-0.0071` n `20`; unknown avg `4.0922` n `1232`
- 4h: commodity avg `-0.0797` n `13`; crypto_alt avg `0.0826` n `239`; crypto_major avg `0.8056` n `8`; equity avg `-0.6506` n `162`; fx avg `-0.0112` n `6`; index avg `-0.0691` n `27`; metal avg `-0.0657` n `20`; unknown avg `383.2986` n `1188`
- 24h: commodity avg `-0.9103` n `13`; crypto_alt avg `-0.5016` n `239`; crypto_major avg `0.0949` n `8`; equity avg `-4.1902` n `162`; fx avg `-0.1177` n `6`; index avg `-0.4825` n `27`; metal avg `-0.6125` n `20`; unknown avg `509.8639` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1469`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
