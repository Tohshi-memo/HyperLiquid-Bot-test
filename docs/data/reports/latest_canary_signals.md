# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T06:22:32.368202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0549` n `13`; crypto_alt avg `-0.0208` n `239`; crypto_major avg `-0.0541` n `8`; equity avg `0.0279` n `163`; fx avg `0.001` n `6`; index avg `0.0139` n `27`; metal avg `-0.0099` n `20`; unknown avg `8.7798` n `1264`
- 1h: commodity avg `-0.0926` n `13`; crypto_alt avg `0.3296` n `239`; crypto_major avg `-0.0736` n `8`; equity avg `-0.1348` n `163`; fx avg `0.0059` n `6`; index avg `0.0064` n `27`; metal avg `-0.1505` n `20`; unknown avg `-0.2092` n `1240`
- 4h: commodity avg `-0.1631` n `13`; crypto_alt avg `0.374` n `239`; crypto_major avg `0.5186` n `8`; equity avg `0.7322` n `163`; fx avg `0.0028` n `6`; index avg `0.1439` n `27`; metal avg `-0.1768` n `20`; unknown avg `3.4552` n `1228`
- 24h: commodity avg `0.0469` n `13`; crypto_alt avg `0.4922` n `239`; crypto_major avg `0.7015` n `8`; equity avg `0.6593` n `163`; fx avg `-0.0937` n `6`; index avg `0.0581` n `27`; metal avg `-0.8484` n `20`; unknown avg `496.5365` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
