# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T11:07:28.046210+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0284` n `12`; crypto_alt avg `0.1145` n `234`; crypto_major avg `0.0606` n `8`; equity avg `0.0518` n `137`; fx avg `-0.0436` n `6`; index avg `0.0253` n `27`; metal avg `0.0578` n `20`; unknown avg `0.0792` n `919`
- 1h: commodity avg `-0.0033` n `12`; crypto_alt avg `0.1148` n `234`; crypto_major avg `-0.1079` n `8`; equity avg `0.1129` n `137`; fx avg `-0.0542` n `6`; index avg `0.035` n `27`; metal avg `0.15` n `20`; unknown avg `0.3023` n `919`
- 4h: commodity avg `-0.1078` n `12`; crypto_alt avg `0.0746` n `234`; crypto_major avg `-0.2524` n `8`; equity avg `0.5308` n `137`; fx avg `0.0045` n `6`; index avg `0.076` n `27`; metal avg `0.0934` n `20`; unknown avg `0.4926` n `911`
- 24h: commodity avg `-0.6517` n `12`; crypto_alt avg `3.0063` n `234`; crypto_major avg `1.1451` n `8`; equity avg `1.5063` n `137`; fx avg `0.0502` n `6`; index avg `0.1365` n `27`; metal avg `-0.1005` n `20`; unknown avg `0.3354` n `721`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
