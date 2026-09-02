# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T22:37:38.554172+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0256` n `12`; crypto_alt avg `0.2094` n `232`; crypto_major avg `0.1792` n `8`; equity avg `0.0041` n `133`; fx avg `0.0017` n `6`; index avg `0.0122` n `26`; metal avg `0.0188` n `20`; unknown avg `0.384` n `792`
- 1h: commodity avg `0.0616` n `12`; crypto_alt avg `-0.0574` n `232`; crypto_major avg `-0.1991` n `8`; equity avg `-0.0217` n `133`; fx avg `0.0059` n `6`; index avg `0.0118` n `26`; metal avg `-0.0064` n `20`; unknown avg `16.543` n `790`
- 4h: commodity avg `0.1478` n `12`; crypto_alt avg `-0.0827` n `232`; crypto_major avg `-0.0139` n `8`; equity avg `0.2802` n `133`; fx avg `-0.0235` n `6`; index avg `0.0247` n `26`; metal avg `0.0373` n `20`; unknown avg `-0.3632` n `772`
- 24h: commodity avg `0.1635` n `12`; crypto_alt avg `-0.0228` n `232`; crypto_major avg `-0.1344` n `8`; equity avg `1.0846` n `133`; fx avg `-0.4017` n `6`; index avg `0.1471` n `26`; metal avg `0.4874` n `20`; unknown avg `-0.4924` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0468`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0445`, n `668`, weak_sample_signal
