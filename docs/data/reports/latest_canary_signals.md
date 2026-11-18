# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T10:07:45.050773+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0378` n `13`; crypto_alt avg `-0.0277` n `239`; crypto_major avg `0.0654` n `8`; equity avg `0.0897` n `163`; fx avg `0.0102` n `6`; index avg `0.014` n `27`; metal avg `-0.0235` n `20`; unknown avg `3.7712` n `1260`
- 1h: commodity avg `0.0516` n `13`; crypto_alt avg `0.0299` n `239`; crypto_major avg `-0.0149` n `8`; equity avg `0.0985` n `163`; fx avg `0.0615` n `6`; index avg `0.026` n `27`; metal avg `0.0523` n `20`; unknown avg `3.7897` n `1262`
- 4h: commodity avg `-0.0702` n `13`; crypto_alt avg `0.1694` n `239`; crypto_major avg `0.0966` n `8`; equity avg `0.7936` n `163`; fx avg `-0.0528` n `6`; index avg `0.1113` n `27`; metal avg `-0.2179` n `20`; unknown avg `68.1206` n `1182`
- 24h: commodity avg `-0.1775` n `13`; crypto_alt avg `1.0784` n `239`; crypto_major avg `1.3749` n `8`; equity avg `2.0593` n `163`; fx avg `-0.0774` n `6`; index avg `0.1961` n `27`; metal avg `-0.8946` n `20`; unknown avg `5.786` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0789`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0617`, n `668`, weak_sample_signal
