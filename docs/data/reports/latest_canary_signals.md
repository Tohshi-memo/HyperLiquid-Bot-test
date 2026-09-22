# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T05:52:27.132637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0011` n `12`; crypto_alt avg `0.7317` n `234`; crypto_major avg `0.5568` n `8`; equity avg `0.2628` n `140`; fx avg `-0.006` n `6`; index avg `0.0349` n `26`; metal avg `0.1041` n `20`; unknown avg `8.9794` n `944`
- 1h: commodity avg `0.0097` n `12`; crypto_alt avg `0.2282` n `234`; crypto_major avg `0.1633` n `8`; equity avg `-0.0559` n `140`; fx avg `-0.007` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0468` n `20`; unknown avg `50.8878` n `942`
- 4h: commodity avg `0.1232` n `12`; crypto_alt avg `0.0618` n `234`; crypto_major avg `0.0203` n `8`; equity avg `-0.571` n `140`; fx avg `-0.0271` n `6`; index avg `-0.0755` n `26`; metal avg `-0.1164` n `20`; unknown avg `61.2754` n `936`
- 24h: commodity avg `-0.2173` n `12`; crypto_alt avg `3.1656` n `234`; crypto_major avg `4.2652` n `8`; equity avg `1.7571` n `140`; fx avg `-0.2512` n `6`; index avg `0.3982` n `26`; metal avg `-0.0558` n `20`; unknown avg `6.1679` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1489`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
