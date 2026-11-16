# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T11:37:24.242122+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0525` n `13`; crypto_alt avg `-0.3044` n `239`; crypto_major avg `-0.2694` n `8`; equity avg `-0.1173` n `162`; fx avg `0.0028` n `6`; index avg `-0.02` n `27`; metal avg `0.0568` n `20`; unknown avg `-0.1326` n `1265`
- 1h: commodity avg `-0.0381` n `13`; crypto_alt avg `0.2934` n `239`; crypto_major avg `0.1951` n `8`; equity avg `0.1222` n `162`; fx avg `-0.0044` n `6`; index avg `0.0011` n `27`; metal avg `0.0822` n `20`; unknown avg `0.0302` n `1263`
- 4h: commodity avg `-0.1607` n `13`; crypto_alt avg `-0.241` n `239`; crypto_major avg `-0.2006` n `8`; equity avg `-0.3026` n `162`; fx avg `-0.0168` n `6`; index avg `-0.0096` n `27`; metal avg `0.0863` n `20`; unknown avg `30.02` n `1219`
- 24h: commodity avg `-0.4033` n `13`; crypto_alt avg `-1.187` n `239`; crypto_major avg `-1.1802` n `8`; equity avg `-0.9487` n `162`; fx avg `-0.0589` n `6`; index avg `-0.0637` n `27`; metal avg `0.0982` n `20`; unknown avg `33.6639` n `1053`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.135`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.115`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.111`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1006`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0964`, n `669`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `669`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0705`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0643`, n `669`, weak_sample_signal
