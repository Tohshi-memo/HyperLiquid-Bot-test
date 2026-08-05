# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T17:07:55.027865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0061` n `12`; crypto_alt avg `0.1526` n `230`; crypto_major avg `0.0884` n `8`; equity avg `-0.2192` n `108`; fx avg `0.0005` n `6`; index avg `-0.021` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0073` n `782`
- 1h: commodity avg `-0.0986` n `12`; crypto_alt avg `0.1976` n `230`; crypto_major avg `0.2249` n `8`; equity avg `0.0257` n `108`; fx avg `-0.0074` n `6`; index avg `0.0244` n `25`; metal avg `0.1043` n `20`; unknown avg `-0.0897` n `782`
- 4h: commodity avg `-0.1793` n `12`; crypto_alt avg `0.1361` n `230`; crypto_major avg `0.4635` n `8`; equity avg `-0.1929` n `108`; fx avg `-0.023` n `6`; index avg `-0.1083` n `25`; metal avg `0.2501` n `20`; unknown avg `-0.0541` n `782`
- 24h: commodity avg `-0.1578` n `12`; crypto_alt avg `0.7116` n `230`; crypto_major avg `0.6252` n `8`; equity avg `-0.1021` n `108`; fx avg `-0.002` n `6`; index avg `0.0108` n `25`; metal avg `0.5987` n `20`; unknown avg `0.6817` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
