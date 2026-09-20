# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T05:07:26.153988+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3172` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `-0.0123` n `234`; crypto_major avg `0.0743` n `8`; equity avg `0.0352` n `140`; fx avg `-0.0011` n `6`; index avg `-0.0027` n `26`; metal avg `0.0033` n `20`; unknown avg `41.0716` n `941`
- 1h: commodity avg `-0.0169` n `12`; crypto_alt avg `0.0018` n `234`; crypto_major avg `0.0055` n `8`; equity avg `-0.0302` n `140`; fx avg `0.0011` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0024` n `20`; unknown avg `10.5476` n `931`
- 4h: commodity avg `0.1979` n `12`; crypto_alt avg `-1.5565` n `234`; crypto_major avg `-1.3904` n `8`; equity avg `-0.4066` n `140`; fx avg `-0.0099` n `6`; index avg `-0.0732` n `26`; metal avg `-0.0262` n `20`; unknown avg `3.6878` n `925`
- 24h: commodity avg `0.233` n `12`; crypto_alt avg `-0.3432` n `234`; crypto_major avg `-1.8516` n `8`; equity avg `-0.2367` n `140`; fx avg `-0.0463` n `6`; index avg `-0.0587` n `26`; metal avg `-0.0075` n `20`; unknown avg `3.4634` n `816`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
