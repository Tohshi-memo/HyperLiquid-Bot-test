# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T04:07:32.568778+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0394` n `12`; crypto_alt avg `0.3859` n `234`; crypto_major avg `0.7996` n `8`; equity avg `-0.1567` n `140`; fx avg `0.0128` n `6`; index avg `-0.0219` n `26`; metal avg `-0.0244` n `20`; unknown avg `1.2297` n `936`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.7157` n `234`; crypto_major avg `1.0723` n `8`; equity avg `-0.2005` n `140`; fx avg `-0.0006` n `6`; index avg `-0.024` n `26`; metal avg `-0.0369` n `20`; unknown avg `1.2727` n `936`
- 4h: commodity avg `0.1828` n `12`; crypto_alt avg `0.2606` n `234`; crypto_major avg `-0.0391` n `8`; equity avg `-0.3232` n `140`; fx avg `-0.0966` n `6`; index avg `-0.0571` n `26`; metal avg `-0.2921` n `20`; unknown avg `1.93` n `936`
- 24h: commodity avg `-0.1572` n `12`; crypto_alt avg `3.4343` n `234`; crypto_major avg `5.2881` n `8`; equity avg `2.2246` n `140`; fx avg `-0.2254` n `6`; index avg `0.4502` n `26`; metal avg `-0.0478` n `20`; unknown avg `8.788` n `772`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.158`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
