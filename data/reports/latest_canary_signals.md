# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T20:07:42.767052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `13`; crypto_alt avg `-0.1769` n `239`; crypto_major avg `-0.1696` n `8`; equity avg `-0.193` n `162`; fx avg `0.0023` n `6`; index avg `-0.0122` n `27`; metal avg `-0.0111` n `20`; unknown avg `1.6924` n `1241`
- 1h: commodity avg `0.2453` n `13`; crypto_alt avg `0.1196` n `239`; crypto_major avg `0.1279` n `8`; equity avg `-0.1451` n `162`; fx avg `0.0137` n `6`; index avg `-0.0172` n `27`; metal avg `-0.005` n `20`; unknown avg `1.7102` n `1241`
- 4h: commodity avg `0.7339` n `13`; crypto_alt avg `-0.059` n `239`; crypto_major avg `-0.3055` n `8`; equity avg `-1.0271` n `162`; fx avg `-0.0129` n `6`; index avg `-0.1113` n `27`; metal avg `0.0034` n `20`; unknown avg `59.5901` n `1229`
- 24h: commodity avg `0.9724` n `13`; crypto_alt avg `-2.6174` n `239`; crypto_major avg `-3.0341` n `8`; equity avg `-2.6956` n `162`; fx avg `-0.144` n `6`; index avg `-0.1693` n `27`; metal avg `-0.7262` n `20`; unknown avg `18.1549` n `1135`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
