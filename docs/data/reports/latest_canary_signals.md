# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T04:07:26.936257+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `0.3024` n `234`; crypto_major avg `0.2234` n `8`; equity avg `0.0359` n `137`; fx avg `-0.0097` n `6`; index avg `0.0081` n `27`; metal avg `0.0258` n `20`; unknown avg `-0.1329` n `917`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.3411` n `234`; crypto_major avg `0.255` n `8`; equity avg `0.2836` n `137`; fx avg `-0.0066` n `6`; index avg `0.0399` n `27`; metal avg `0.0173` n `20`; unknown avg `0.1498` n `917`
- 4h: commodity avg `-0.1091` n `12`; crypto_alt avg `-0.103` n `234`; crypto_major avg `0.3974` n `8`; equity avg `0.7206` n `137`; fx avg `0.0427` n `6`; index avg `0.1057` n `27`; metal avg `0.2956` n `20`; unknown avg `0.0965` n `907`
- 24h: commodity avg `0.2118` n `12`; crypto_alt avg `-3.2009` n `234`; crypto_major avg `-3.2308` n `8`; equity avg `-0.5862` n `137`; fx avg `0.2254` n `6`; index avg `-0.0139` n `27`; metal avg `0.3594` n `20`; unknown avg `18796.3791` n `802`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0753`, n `668`, weak_sample_signal
