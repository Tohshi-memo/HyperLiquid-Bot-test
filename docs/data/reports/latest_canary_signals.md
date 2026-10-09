# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T16:07:30.480809+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.08` n `13`; crypto_alt avg `0.2834` n `235`; crypto_major avg `0.0886` n `8`; equity avg `-0.0593` n `150`; fx avg `-0.012` n `6`; index avg `0.0046` n `26`; metal avg `0.0` n `20`; unknown avg `0.0257` n `1076`
- 1h: commodity avg `-0.1217` n `13`; crypto_alt avg `0.7241` n `235`; crypto_major avg `0.2037` n `8`; equity avg `0.0799` n `150`; fx avg `-0.0014` n `6`; index avg `0.0267` n `26`; metal avg `0.0555` n `20`; unknown avg `0.8245` n `1020`
- 4h: commodity avg `0.3835` n `13`; crypto_alt avg `0.1885` n `235`; crypto_major avg `-0.5964` n `8`; equity avg `-0.5412` n `150`; fx avg `0.003` n `6`; index avg `-0.0655` n `26`; metal avg `0.066` n `20`; unknown avg `0.1859` n `996`
- 24h: commodity avg `-0.1043` n `13`; crypto_alt avg `3.6872` n `235`; crypto_major avg `1.918` n `8`; equity avg `0.1405` n `150`; fx avg `0.0168` n `6`; index avg `0.0644` n `26`; metal avg `0.8308` n `20`; unknown avg `1.4297` n `915`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
