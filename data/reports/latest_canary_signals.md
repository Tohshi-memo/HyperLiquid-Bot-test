# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T04:52:29.309868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1565` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0096` n `13`; crypto_alt avg `0.1901` n `238`; crypto_major avg `0.2042` n `8`; equity avg `0.164` n `155`; fx avg `-0.0028` n `6`; index avg `0.0382` n `27`; metal avg `0.0282` n `20`; unknown avg `0.1269` n `1234`
- 1h: commodity avg `0.0195` n `13`; crypto_alt avg `0.4457` n `238`; crypto_major avg `0.5871` n `8`; equity avg `0.4183` n `155`; fx avg `0.017` n `6`; index avg `0.1035` n `27`; metal avg `0.0038` n `20`; unknown avg `0.4121` n `1216`
- 4h: commodity avg `-0.0217` n `13`; crypto_alt avg `-2.1431` n `238`; crypto_major avg `-1.2603` n `8`; equity avg `-0.9436` n `155`; fx avg `0.0089` n `6`; index avg `-0.1038` n `27`; metal avg `-0.1438` n `20`; unknown avg `2.5447` n `1198`
- 24h: commodity avg `-0.1003` n `13`; crypto_alt avg `-2.2147` n `238`; crypto_major avg `-1.3382` n `8`; equity avg `-0.8847` n `154`; fx avg `-0.0134` n `6`; index avg `0.0013` n `27`; metal avg `-0.2061` n `20`; unknown avg `26.9179` n `976`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
