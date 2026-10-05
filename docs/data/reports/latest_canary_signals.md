# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T19:53:18.040834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0103` n `13`; crypto_alt avg `0.0072` n `235`; crypto_major avg `0.1946` n `8`; equity avg `0.0271` n `144`; fx avg `0.0097` n `6`; index avg `-0.0287` n `26`; metal avg `-0.0313` n `20`; unknown avg `37.3124` n `1079`
- 1h: commodity avg `-0.0019` n `13`; crypto_alt avg `0.1076` n `235`; crypto_major avg `0.1819` n `8`; equity avg `0.0816` n `144`; fx avg `0.018` n `6`; index avg `-0.0136` n `26`; metal avg `-0.0312` n `20`; unknown avg `23.6472` n `1077`
- 4h: commodity avg `-0.2175` n `13`; crypto_alt avg `0.4507` n `235`; crypto_major avg `0.4382` n `8`; equity avg `0.0211` n `144`; fx avg `0.0114` n `6`; index avg `0.0283` n `26`; metal avg `-0.0` n `20`; unknown avg `10.5323` n `1071`
- 24h: commodity avg `-0.4476` n `13`; crypto_alt avg `0.0588` n `235`; crypto_major avg `0.2957` n `8`; equity avg `0.3068` n `144`; fx avg `-0.069` n `6`; index avg `0.1134` n `26`; metal avg `0.1609` n `20`; unknown avg `6.7875` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2002`, n `670`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1801`, n `670`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.171`, n `670`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1253`, n `670`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1051`, n `670`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1001`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0979`, n `670`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0956`, n `670`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0932`, n `670`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `670`, weak_sample_signal
