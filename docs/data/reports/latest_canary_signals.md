# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T12:07:28.300353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0789` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0499` n `13`; crypto_alt avg `0.1405` n `235`; crypto_major avg `0.087` n `8`; equity avg `0.1029` n `150`; fx avg `-0.0223` n `6`; index avg `0.024` n `26`; metal avg `0.0398` n `20`; unknown avg `0.1292` n `1068`
- 1h: commodity avg `-0.07` n `13`; crypto_alt avg `-0.4604` n `235`; crypto_major avg `-0.2863` n `8`; equity avg `-0.0376` n `150`; fx avg `-0.038` n `6`; index avg `-0.0158` n `26`; metal avg `0.0341` n `20`; unknown avg `1.4626` n `1068`
- 4h: commodity avg `0.1146` n `13`; crypto_alt avg `-1.6693` n `235`; crypto_major avg `-1.2191` n `8`; equity avg `-0.8158` n `150`; fx avg `-0.0104` n `6`; index avg `-0.1402` n `26`; metal avg `-0.2097` n `20`; unknown avg `1.4216` n `1068`
- 24h: commodity avg `1.4056` n `13`; crypto_alt avg `-5.3877` n `235`; crypto_major avg `-3.7155` n `8`; equity avg `-1.6864` n `150`; fx avg `-0.1976` n `6`; index avg `-0.383` n `26`; metal avg `-0.5672` n `20`; unknown avg `815.8401` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
