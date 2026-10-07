# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T08:07:32.948796+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.1958` n `235`; crypto_major avg `-0.0796` n `8`; equity avg `-0.0508` n `150`; fx avg `-0.0561` n `6`; index avg `0.0114` n `26`; metal avg `0.0042` n `20`; unknown avg `-0.011` n `1058`
- 1h: commodity avg `0.0881` n `13`; crypto_alt avg `-0.1413` n `235`; crypto_major avg `-0.0173` n `8`; equity avg `-0.2459` n `150`; fx avg `-0.1344` n `6`; index avg `-0.0302` n `26`; metal avg `0.0055` n `20`; unknown avg `0.1372` n `1058`
- 4h: commodity avg `0.1281` n `13`; crypto_alt avg `0.4596` n `235`; crypto_major avg `0.4357` n `8`; equity avg `-0.2872` n `150`; fx avg `-0.1498` n `6`; index avg `-0.0675` n `26`; metal avg `-0.1451` n `20`; unknown avg `0.1879` n `1036`
- 24h: commodity avg `0.8995` n `13`; crypto_alt avg `-3.382` n `235`; crypto_major avg `-2.1635` n `8`; equity avg `-0.5092` n `149`; fx avg `-0.0971` n `6`; index avg `-0.1403` n `26`; metal avg `-0.2211` n `20`; unknown avg `814.5902` n `978`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
