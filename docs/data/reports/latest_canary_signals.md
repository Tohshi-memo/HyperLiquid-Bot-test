# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T04:22:26.225838+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0467` n `13`; crypto_alt avg `-0.0668` n `239`; crypto_major avg `-0.1372` n `8`; equity avg `-0.054` n `161`; fx avg `-0.0134` n `6`; index avg `-0.0105` n `27`; metal avg `-0.0173` n `20`; unknown avg `1.739` n `1258`
- 1h: commodity avg `-0.0601` n `13`; crypto_alt avg `0.0025` n `239`; crypto_major avg `-0.0251` n `8`; equity avg `-0.1734` n `161`; fx avg `-0.0215` n `6`; index avg `-0.0053` n `27`; metal avg `0.0148` n `20`; unknown avg `-0.1195` n `1242`
- 4h: commodity avg `-0.1452` n `13`; crypto_alt avg `-0.5996` n `239`; crypto_major avg `-0.4686` n `8`; equity avg `-0.1004` n `161`; fx avg `-0.0719` n `6`; index avg `0.0168` n `27`; metal avg `0.046` n `20`; unknown avg `21.5166` n `1242`
- 24h: commodity avg `0.005` n `13`; crypto_alt avg `-1.597` n `239`; crypto_major avg `-0.1161` n `8`; equity avg `0.5908` n `161`; fx avg `-0.2297` n `6`; index avg `0.0477` n `27`; metal avg `-0.3952` n `20`; unknown avg `1.5748` n `1133`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.179`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
