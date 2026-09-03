# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T00:07:30.296125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `12`; crypto_alt avg `0.0924` n `232`; crypto_major avg `-0.0172` n `8`; equity avg `0.0212` n `133`; fx avg `0.0498` n `6`; index avg `-0.053` n `26`; metal avg `-0.0247` n `20`; unknown avg `0.0232` n `790`
- 1h: commodity avg `0.001` n `12`; crypto_alt avg `0.2455` n `232`; crypto_major avg `0.245` n `8`; equity avg `0.0848` n `133`; fx avg `0.0546` n `6`; index avg `-0.0436` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.1931` n `790`
- 4h: commodity avg `0.0986` n `12`; crypto_alt avg `0.141` n `232`; crypto_major avg `0.1398` n `8`; equity avg `0.1478` n `133`; fx avg `0.0623` n `6`; index avg `-0.0295` n `26`; metal avg `-0.0496` n `20`; unknown avg `16.4839` n `776`
- 24h: commodity avg `0.0611` n `12`; crypto_alt avg `-0.0388` n `232`; crypto_major avg `-0.2502` n `8`; equity avg `1.185` n `133`; fx avg `-0.2828` n `6`; index avg `0.0809` n `26`; metal avg `0.4875` n `20`; unknown avg `-0.2182` n `751`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.052`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0477`, n `668`, weak_sample_signal
