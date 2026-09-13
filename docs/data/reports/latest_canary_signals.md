# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T16:22:31.639538+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0101` n `12`; crypto_alt avg `-0.0098` n `233`; crypto_major avg `0.1245` n `8`; equity avg `0.117` n `136`; fx avg `-0.0007` n `6`; index avg `0.004` n `27`; metal avg `0.0002` n `20`; unknown avg `4.6958` n `838`
- 1h: commodity avg `-0.0111` n `12`; crypto_alt avg `0.0219` n `233`; crypto_major avg `0.3412` n `8`; equity avg `0.1783` n `136`; fx avg `-0.0017` n `6`; index avg `0.0219` n `27`; metal avg `0.0069` n `20`; unknown avg `1.4023` n `836`
- 4h: commodity avg `0.0211` n `12`; crypto_alt avg `0.155` n `233`; crypto_major avg `0.5986` n `8`; equity avg `0.3158` n `136`; fx avg `0.0077` n `6`; index avg `0.058` n `27`; metal avg `0.0074` n `20`; unknown avg `2.0394` n `830`
- 24h: commodity avg `0.2982` n `12`; crypto_alt avg `-0.6881` n `233`; crypto_major avg `-1.2213` n `8`; equity avg `-1.5474` n `136`; fx avg `0.0117` n `6`; index avg `-0.2554` n `26`; metal avg `-0.086` n `20`; unknown avg `0.1811` n `708`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
