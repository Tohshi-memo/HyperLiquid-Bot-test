# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T20:07:41.748461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0132` n `12`; crypto_alt avg `-0.0459` n `230`; crypto_major avg `-0.1007` n `8`; equity avg `-0.3898` n `102`; fx avg `-0.0121` n `6`; index avg `-0.0694` n `25`; metal avg `-0.0593` n `20`; unknown avg `-0.0912` n `780`
- 1h: commodity avg `0.0542` n `12`; crypto_alt avg `-0.2302` n `230`; crypto_major avg `-0.3128` n `8`; equity avg `-0.5913` n `102`; fx avg `-0.0035` n `6`; index avg `-0.0459` n `25`; metal avg `-0.0586` n `20`; unknown avg `-0.2556` n `780`
- 4h: commodity avg `0.1705` n `12`; crypto_alt avg `0.0019` n `230`; crypto_major avg `-0.2837` n `8`; equity avg `0.2381` n `102`; fx avg `0.0778` n `6`; index avg `0.0948` n `25`; metal avg `0.0906` n `20`; unknown avg `7.0632` n `780`
- 24h: commodity avg `0.2569` n `12`; crypto_alt avg `-0.8255` n `230`; crypto_major avg `-2.3736` n `8`; equity avg `-0.7962` n `102`; fx avg `0.215` n `6`; index avg `0.0901` n `25`; metal avg `-0.446` n `20`; unknown avg `0.2039` n `747`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
