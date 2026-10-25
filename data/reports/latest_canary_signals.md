# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T13:07:42.423184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.0779` n `237`; crypto_major avg `0.011` n `8`; equity avg `0.0074` n `152`; fx avg `-0.0028` n `6`; index avg `-0.0001` n `26`; metal avg `0.0017` n `20`; unknown avg `1.5078` n `1229`
- 1h: commodity avg `-0.021` n `13`; crypto_alt avg `-0.0814` n `237`; crypto_major avg `-0.0977` n `8`; equity avg `0.0155` n `152`; fx avg `-0.0055` n `6`; index avg `0.0079` n `26`; metal avg `0.0057` n `20`; unknown avg `1.4038` n `1231`
- 4h: commodity avg `-0.0335` n `13`; crypto_alt avg `0.505` n `237`; crypto_major avg `0.2242` n `8`; equity avg `0.2367` n `152`; fx avg `0.0029` n `6`; index avg `0.0233` n `26`; metal avg `0.033` n `20`; unknown avg `14.4437` n `1195`
- 24h: commodity avg `-0.1628` n `13`; crypto_alt avg `-1.3835` n `237`; crypto_major avg `-0.1475` n `8`; equity avg `0.0436` n `152`; fx avg `-0.0009` n `6`; index avg `0.0348` n `26`; metal avg `-0.0302` n `20`; unknown avg `17.4354` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
