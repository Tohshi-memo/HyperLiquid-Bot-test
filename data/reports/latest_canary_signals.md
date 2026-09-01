# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T18:07:23.110343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2694` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0135` n `12`; crypto_alt avg `-0.1893` n `232`; crypto_major avg `-0.1507` n `8`; equity avg `-0.001` n `131`; fx avg `-0.0016` n `6`; index avg `-0.0145` n `26`; metal avg `-0.0461` n `20`; unknown avg `-0.1611` n `791`
- 1h: commodity avg `0.0936` n `12`; crypto_alt avg `-0.1587` n `232`; crypto_major avg `-0.3054` n `8`; equity avg `-0.0782` n `131`; fx avg `0.0228` n `6`; index avg `-0.0394` n `26`; metal avg `-0.0882` n `20`; unknown avg `-0.5961` n `791`
- 4h: commodity avg `0.5001` n `12`; crypto_alt avg `-1.1843` n `232`; crypto_major avg `-1.3752` n `8`; equity avg `-0.2105` n `131`; fx avg `-0.0046` n `6`; index avg `-0.1058` n `26`; metal avg `-0.1883` n `20`; unknown avg `-1.1302` n `790`
- 24h: commodity avg `0.7908` n `12`; crypto_alt avg `-0.3276` n `232`; crypto_major avg `-1.8341` n `8`; equity avg `-1.583` n `130`; fx avg `0.0411` n `6`; index avg `-0.2835` n `26`; metal avg `-0.6895` n `20`; unknown avg `0.2355` n `752`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0493`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0374`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0368`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0362`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0353`, n `668`, weak_sample_signal
