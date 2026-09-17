# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T05:37:31.089508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0764` n `12`; crypto_alt avg `0.0466` n `234`; crypto_major avg `-0.0626` n `8`; equity avg `-0.1087` n `137`; fx avg `0.0037` n `6`; index avg `-0.0203` n `27`; metal avg `0.0176` n `20`; unknown avg `0.6246` n `921`
- 1h: commodity avg `-0.0846` n `12`; crypto_alt avg `0.3764` n `234`; crypto_major avg `0.1308` n `8`; equity avg `-0.1298` n `137`; fx avg `0.0191` n `6`; index avg `-0.0487` n `27`; metal avg `-0.0267` n `20`; unknown avg `2.1235` n `919`
- 4h: commodity avg `-0.0474` n `12`; crypto_alt avg `0.2718` n `234`; crypto_major avg `-0.3195` n `8`; equity avg `-0.1458` n `137`; fx avg `0.0416` n `6`; index avg `-0.0692` n `27`; metal avg `-0.0951` n `20`; unknown avg `0.3326` n `911`
- 24h: commodity avg `-0.4549` n `12`; crypto_alt avg `2.3696` n `234`; crypto_major avg `1.1253` n `8`; equity avg `1.0137` n `137`; fx avg `0.0212` n `6`; index avg `0.0597` n `27`; metal avg `-0.2502` n `20`; unknown avg `0.3945` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
