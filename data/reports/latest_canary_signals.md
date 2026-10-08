# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T07:37:28.814601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0473` n `13`; crypto_alt avg `0.029` n `235`; crypto_major avg `0.0611` n `8`; equity avg `-0.0097` n `150`; fx avg `-0.0002` n `6`; index avg `-0.0095` n `26`; metal avg `-0.0368` n `20`; unknown avg `-0.0785` n `1077`
- 1h: commodity avg `0.0814` n `13`; crypto_alt avg `0.8543` n `235`; crypto_major avg `0.6402` n `8`; equity avg `-0.0809` n `150`; fx avg `0.0212` n `6`; index avg `-0.0255` n `26`; metal avg `0.017` n `20`; unknown avg `0.2867` n `1075`
- 4h: commodity avg `0.4326` n `13`; crypto_alt avg `0.1308` n `235`; crypto_major avg `-0.0788` n `8`; equity avg `-0.7232` n `150`; fx avg `-0.0064` n `6`; index avg `-0.1418` n `26`; metal avg `-0.2122` n `20`; unknown avg `0.342` n `1041`
- 24h: commodity avg `0.7615` n `13`; crypto_alt avg `-0.7857` n `235`; crypto_major avg `-2.0486` n `8`; equity avg `-1.8593` n `150`; fx avg `-0.0571` n `6`; index avg `-0.328` n `26`; metal avg `-0.2576` n `20`; unknown avg `416.814` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
