# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T05:22:23.562577+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `13`; crypto_alt avg `0.1518` n `235`; crypto_major avg `0.0749` n `8`; equity avg `-0.0051` n `150`; fx avg `-0.0014` n `6`; index avg `0.0003` n `26`; metal avg `-0.003` n `20`; unknown avg `-0.0023` n `1116`
- 1h: commodity avg `0.0378` n `13`; crypto_alt avg `0.4148` n `235`; crypto_major avg `0.1795` n `8`; equity avg `0.0028` n `150`; fx avg `-0.0012` n `6`; index avg `0.0071` n `26`; metal avg `-0.0125` n `20`; unknown avg `0.8924` n `1114`
- 4h: commodity avg `0.0362` n `13`; crypto_alt avg `0.7803` n `235`; crypto_major avg `0.2828` n `8`; equity avg `0.0571` n `150`; fx avg `0.0032` n `6`; index avg `0.0132` n `26`; metal avg `-0.0178` n `20`; unknown avg `-0.2073` n `1108`
- 24h: commodity avg `0.0545` n `13`; crypto_alt avg `2.0152` n `235`; crypto_major avg `0.1323` n `8`; equity avg `0.1969` n `150`; fx avg `-0.0218` n `6`; index avg `0.0498` n `26`; metal avg `0.0851` n `20`; unknown avg `12.7301` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
