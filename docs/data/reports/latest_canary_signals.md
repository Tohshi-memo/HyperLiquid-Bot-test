# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T00:22:26.716921+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0137` n `12`; crypto_alt avg `-0.1046` n `234`; crypto_major avg `-0.1046` n `8`; equity avg `0.0198` n `141`; fx avg `0.0049` n `6`; index avg `0.0024` n `26`; metal avg `0.0036` n `20`; unknown avg `0.0379` n `959`
- 1h: commodity avg `-0.0536` n `12`; crypto_alt avg `-0.215` n `234`; crypto_major avg `-0.1784` n `8`; equity avg `0.0376` n `141`; fx avg `0.0057` n `6`; index avg `0.0092` n `26`; metal avg `0.005` n `20`; unknown avg `2.4813` n `951`
- 4h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1068` n `234`; crypto_major avg `0.2118` n `8`; equity avg `0.0956` n `141`; fx avg `-0.0086` n `6`; index avg `0.0076` n `26`; metal avg `0.0065` n `20`; unknown avg `7.1184` n `927`
- 24h: commodity avg `0.2827` n `12`; crypto_alt avg `0.0528` n `234`; crypto_major avg `-0.8591` n `8`; equity avg `0.0532` n `141`; fx avg `0.0155` n `6`; index avg `-0.0502` n `26`; metal avg `-0.0185` n `20`; unknown avg `4.1385` n `886`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
