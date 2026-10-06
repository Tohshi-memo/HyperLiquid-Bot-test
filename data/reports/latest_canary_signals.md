# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T23:07:25.509130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `13`; crypto_alt avg `0.1053` n `235`; crypto_major avg `-0.0283` n `8`; equity avg `0.0273` n `150`; fx avg `0.0022` n `6`; index avg `0.0051` n `26`; metal avg `0.0156` n `20`; unknown avg `0.3718` n `1074`
- 1h: commodity avg `0.0197` n `13`; crypto_alt avg `-0.1039` n `235`; crypto_major avg `-0.1526` n `8`; equity avg `-0.0122` n `150`; fx avg `0.0044` n `6`; index avg `-0.0039` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.3242` n `1074`
- 4h: commodity avg `0.0965` n `13`; crypto_alt avg `-0.2845` n `235`; crypto_major avg `-0.104` n `8`; equity avg `-0.022` n `150`; fx avg `0.0018` n `6`; index avg `-0.0079` n `26`; metal avg `-0.0955` n `20`; unknown avg `0.6615` n `990`
- 24h: commodity avg `0.3118` n `13`; crypto_alt avg `-1.403` n `235`; crypto_major avg `-1.1269` n `8`; equity avg `0.3592` n `149`; fx avg `0.093` n `6`; index avg `-0.0082` n `26`; metal avg `0.0478` n `20`; unknown avg `871.4157` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1655`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
