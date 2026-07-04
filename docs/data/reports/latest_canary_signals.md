# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T00:37:26.000902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0121` n `12`; crypto_alt avg `0.0583` n `229`; crypto_major avg `0.0528` n `8`; equity avg `-0.0248` n `88`; fx avg `0.0015` n `6`; index avg `-0.0353` n `25`; metal avg `-0.0082` n `20`; unknown avg `0.6573` n `765`
- 1h: commodity avg `0.0484` n `12`; crypto_alt avg `0.0109` n `229`; crypto_major avg `0.0815` n `8`; equity avg `-0.0275` n `88`; fx avg `0.0121` n `6`; index avg `-0.0419` n `25`; metal avg `-0.0348` n `20`; unknown avg `0.7574` n `765`
- 4h: commodity avg `0.0524` n `12`; crypto_alt avg `-0.2081` n `229`; crypto_major avg `-0.1099` n `8`; equity avg `-0.0167` n `88`; fx avg `0.0089` n `6`; index avg `-0.0591` n `25`; metal avg `-0.0062` n `20`; unknown avg `0.9651` n `765`
- 24h: commodity avg `0.1958` n `12`; crypto_alt avg `3.1913` n `229`; crypto_major avg `3.5158` n `8`; equity avg `1.7213` n `88`; fx avg `-0.1653` n `6`; index avg `0.3979` n `25`; metal avg `0.3646` n `20`; unknown avg `6.5754` n `739`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
