# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T23:07:25.979408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `13`; crypto_alt avg `0.0512` n `235`; crypto_major avg `0.0106` n `8`; equity avg `0.0907` n `150`; fx avg `-0.0003` n `6`; index avg `0.0044` n `26`; metal avg `0.0187` n `20`; unknown avg `0.0041` n `1075`
- 1h: commodity avg `-0.0482` n `13`; crypto_alt avg `0.4889` n `235`; crypto_major avg `0.1546` n `8`; equity avg `0.0968` n `150`; fx avg `0.0095` n `6`; index avg `0.0046` n `26`; metal avg `0.0076` n `20`; unknown avg `0.1291` n `1075`
- 4h: commodity avg `0.1344` n `13`; crypto_alt avg `0.8219` n `235`; crypto_major avg `-0.0126` n `8`; equity avg `0.2562` n `150`; fx avg `0.0231` n `6`; index avg `0.0445` n `26`; metal avg `0.0457` n `20`; unknown avg `-0.0905` n `999`
- 24h: commodity avg `0.4445` n `13`; crypto_alt avg `-3.7294` n `235`; crypto_major avg `-3.3814` n `8`; equity avg `-1.2902` n `150`; fx avg `-0.1451` n `6`; index avg `-0.2003` n `26`; metal avg `-0.679` n `20`; unknown avg `247.588` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
