# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T01:07:35.394538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0756` n `12`; crypto_alt avg `0.0949` n `234`; crypto_major avg `-0.0084` n `8`; equity avg `0.1097` n `137`; fx avg `0.0222` n `6`; index avg `0.0381` n `27`; metal avg `0.2217` n `20`; unknown avg `1.8264` n `917`
- 1h: commodity avg `-0.0484` n `12`; crypto_alt avg `0.1285` n `234`; crypto_major avg `0.018` n `8`; equity avg `-0.0133` n `137`; fx avg `0.0501` n `6`; index avg `-0.0072` n `27`; metal avg `0.2074` n `20`; unknown avg `2.2358` n `911`
- 4h: commodity avg `-0.1353` n `12`; crypto_alt avg `1.1868` n `234`; crypto_major avg `0.1539` n `8`; equity avg `0.8215` n `137`; fx avg `0.012` n `6`; index avg `0.1757` n `27`; metal avg `0.2974` n `20`; unknown avg `2.002` n `813`
- 24h: commodity avg `-0.6499` n `12`; crypto_alt avg `1.7556` n `234`; crypto_major avg `1.0859` n `8`; equity avg `1.7474` n `137`; fx avg `-0.0192` n `6`; index avg `0.2059` n `27`; metal avg `0.083` n `20`; unknown avg `1.1251` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
