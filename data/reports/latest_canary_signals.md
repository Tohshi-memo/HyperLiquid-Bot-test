# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T12:22:31.116437+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0299` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0203` n `13`; crypto_alt avg `0.0575` n `235`; crypto_major avg `-0.0294` n `8`; equity avg `-0.135` n `150`; fx avg `-0.0056` n `6`; index avg `-0.0298` n `26`; metal avg `-0.0738` n `20`; unknown avg `-0.0765` n `1076`
- 1h: commodity avg `-0.0818` n `13`; crypto_alt avg `-0.1323` n `235`; crypto_major avg `-0.1448` n `8`; equity avg `-0.1418` n `150`; fx avg `-0.0424` n `6`; index avg `-0.0373` n `26`; metal avg `-0.0534` n `20`; unknown avg `2.2358` n `1068`
- 4h: commodity avg `0.1684` n `13`; crypto_alt avg `-1.5442` n `235`; crypto_major avg `-1.2142` n `8`; equity avg `-0.968` n `150`; fx avg `-0.0351` n `6`; index avg `-0.1843` n `26`; metal avg `-0.2651` n `20`; unknown avg `1.9514` n `1068`
- 24h: commodity avg `1.4709` n `13`; crypto_alt avg `-5.2605` n `235`; crypto_major avg `-3.6648` n `8`; equity avg `-1.784` n `150`; fx avg `-0.2174` n `6`; index avg `-0.4081` n `26`; metal avg `-0.6233` n `20`; unknown avg `816.3726` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
