# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T06:37:04.579477+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0327` n `13`; crypto_alt avg `0.2283` n `235`; crypto_major avg `0.2101` n `8`; equity avg `0.0086` n `150`; fx avg `0.0024` n `6`; index avg `-0.0009` n `26`; metal avg `-0.0173` n `20`; unknown avg `0.4274` n `1076`
- 1h: commodity avg `0.0476` n `13`; crypto_alt avg `0.1783` n `235`; crypto_major avg `0.2598` n `8`; equity avg `-0.0754` n `150`; fx avg `0.0126` n `6`; index avg `-0.0292` n `26`; metal avg `-0.0815` n `20`; unknown avg `0.3757` n `1052`
- 4h: commodity avg `0.1156` n `13`; crypto_alt avg `-0.1498` n `235`; crypto_major avg `0.4903` n `8`; equity avg `-0.0085` n `150`; fx avg `-0.0216` n `6`; index avg `-0.0399` n `26`; metal avg `-0.1684` n `20`; unknown avg `0.6697` n `1046`
- 24h: commodity avg `0.806` n `13`; crypto_alt avg `-2.8614` n `235`; crypto_major avg `-1.6804` n `8`; equity avg `-0.225` n `149`; fx avg `0.0504` n `6`; index avg `-0.091` n `26`; metal avg `-0.1616` n `20`; unknown avg `870.9482` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
