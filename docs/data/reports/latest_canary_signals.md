# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T00:07:26.882523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0272` n `12`; crypto_alt avg `0.2426` n `234`; crypto_major avg `0.202` n `8`; equity avg `-0.0713` n `141`; fx avg `0.0101` n `6`; index avg `-0.0119` n `26`; metal avg `-0.025` n `20`; unknown avg `0.1283` n `937`
- 1h: commodity avg `-0.0041` n `12`; crypto_alt avg `0.2458` n `234`; crypto_major avg `0.1437` n `8`; equity avg `-0.1357` n `141`; fx avg `0.0013` n `6`; index avg `-0.0422` n `26`; metal avg `-0.0569` n `20`; unknown avg `-0.1569` n `937`
- 4h: commodity avg `-0.0765` n `12`; crypto_alt avg `0.256` n `234`; crypto_major avg `0.4525` n `8`; equity avg `0.0459` n `141`; fx avg `-0.0172` n `6`; index avg `-0.0205` n `26`; metal avg `-0.0167` n `20`; unknown avg `-0.6398` n `869`
- 24h: commodity avg `0.4641` n `12`; crypto_alt avg `-4.3426` n `234`; crypto_major avg `-3.0507` n `8`; equity avg `-1.6818` n `140`; fx avg `0.0341` n `6`; index avg `-0.386` n `26`; metal avg `-0.8819` n `20`; unknown avg `583.1236` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
