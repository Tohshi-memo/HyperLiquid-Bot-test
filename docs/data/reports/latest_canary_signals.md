# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T03:22:30.617387+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0419` n `12`; crypto_alt avg `0.3307` n `234`; crypto_major avg `0.3417` n `8`; equity avg `0.1859` n `137`; fx avg `0.0057` n `6`; index avg `0.038` n `27`; metal avg `0.0563` n `20`; unknown avg `0.3502` n `919`
- 1h: commodity avg `-0.1055` n `12`; crypto_alt avg `0.4442` n `234`; crypto_major avg `0.4314` n `8`; equity avg `0.6474` n `137`; fx avg `-0.0148` n `6`; index avg `0.1019` n `27`; metal avg `0.2981` n `20`; unknown avg `5.9886` n `913`
- 4h: commodity avg `-0.1925` n `12`; crypto_alt avg `-0.3963` n `234`; crypto_major avg `0.0403` n `8`; equity avg `0.593` n `137`; fx avg `0.0815` n `6`; index avg `0.1064` n `27`; metal avg `0.3193` n `20`; unknown avg `4.6744` n `907`
- 24h: commodity avg `0.1917` n `12`; crypto_alt avg `-3.1701` n `234`; crypto_major avg `-3.0993` n `8`; equity avg `-0.8031` n `137`; fx avg `0.2236` n `6`; index avg `-0.0472` n `27`; metal avg `0.3603` n `20`; unknown avg `0.839` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
