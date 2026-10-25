# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T16:37:21.615672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `13`; crypto_alt avg `0.1145` n `237`; crypto_major avg `-0.0183` n `8`; equity avg `0.0564` n `152`; fx avg `-0.0007` n `6`; index avg `0.0094` n `26`; metal avg `0.0079` n `20`; unknown avg `0.9511` n `1240`
- 1h: commodity avg `-0.0113` n `13`; crypto_alt avg `-0.1889` n `237`; crypto_major avg `-0.2294` n `8`; equity avg `0.1038` n `152`; fx avg `-0.0082` n `6`; index avg `0.0138` n `26`; metal avg `0.0117` n `20`; unknown avg `0.1969` n `1234`
- 4h: commodity avg `-0.0825` n `13`; crypto_alt avg `0.5123` n `237`; crypto_major avg `0.3053` n `8`; equity avg `0.3679` n `152`; fx avg `-0.0208` n `6`; index avg `0.059` n `26`; metal avg `0.057` n `20`; unknown avg `1.2651` n `1225`
- 24h: commodity avg `-0.2243` n `13`; crypto_alt avg `1.2372` n `237`; crypto_major avg `1.7549` n `8`; equity avg `1.0302` n `152`; fx avg `0.0132` n `6`; index avg `0.1766` n `26`; metal avg `0.1694` n `20`; unknown avg `10.0165` n `1081`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1688`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1114`, n `668`, weak_sample_signal
