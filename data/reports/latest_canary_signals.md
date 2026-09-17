# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T00:22:26.649594+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `12`; crypto_alt avg `0.1929` n `234`; crypto_major avg `0.164` n `8`; equity avg `-0.1116` n `137`; fx avg `0.0185` n `6`; index avg `-0.0415` n `27`; metal avg `0.0549` n `20`; unknown avg `0.2263` n `919`
- 1h: commodity avg `-0.0858` n `12`; crypto_alt avg `0.7688` n `234`; crypto_major avg `0.3354` n `8`; equity avg `0.2015` n `137`; fx avg `-0.0222` n `6`; index avg `0.0615` n `27`; metal avg `0.0971` n `20`; unknown avg `0.0448` n `915`
- 4h: commodity avg `-0.0705` n `12`; crypto_alt avg `1.3692` n `234`; crypto_major avg `-0.0162` n `8`; equity avg `0.7629` n `137`; fx avg `-0.0457` n `6`; index avg `0.1527` n `27`; metal avg `0.1785` n `20`; unknown avg `0.7176` n `813`
- 24h: commodity avg `-0.5837` n `12`; crypto_alt avg `1.4955` n `234`; crypto_major avg `1.1663` n `8`; equity avg `1.5123` n `137`; fx avg `0.0125` n `6`; index avg `0.1503` n `27`; metal avg `-0.1064` n `20`; unknown avg `-0.1575` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
