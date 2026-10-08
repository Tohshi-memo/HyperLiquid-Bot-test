# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T07:52:29.111297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `13`; crypto_alt avg `-0.3678` n `235`; crypto_major avg `-0.2414` n `8`; equity avg `-0.0496` n `150`; fx avg `0.0085` n `6`; index avg `-0.002` n `26`; metal avg `-0.0307` n `20`; unknown avg `4.832` n `1077`
- 1h: commodity avg `0.1689` n `13`; crypto_alt avg `0.1711` n `235`; crypto_major avg `0.1806` n `8`; equity avg `-0.1053` n `150`; fx avg `0.0129` n `6`; index avg `-0.0119` n `26`; metal avg `-0.0693` n `20`; unknown avg `4.0916` n `1075`
- 4h: commodity avg `0.4174` n `13`; crypto_alt avg `-0.0992` n `235`; crypto_major avg `-0.1816` n `8`; equity avg `-0.6174` n `150`; fx avg `0.0071` n `6`; index avg `-0.1161` n `26`; metal avg `-0.2412` n `20`; unknown avg `2.1522` n `1041`
- 24h: commodity avg `0.6838` n `13`; crypto_alt avg `-1.1577` n `235`; crypto_major avg `-2.2752` n `8`; equity avg `-1.8595` n `150`; fx avg `-0.038` n `6`; index avg `-0.3062` n `26`; metal avg `-0.2855` n `20`; unknown avg `416.6948` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
