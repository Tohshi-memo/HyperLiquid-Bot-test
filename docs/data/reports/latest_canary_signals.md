# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T19:07:25.661663+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `12`; crypto_alt avg `0.022` n `230`; crypto_major avg `-0.0384` n `8`; equity avg `0.0161` n `103`; fx avg `-0.0017` n `6`; index avg `0.0275` n `25`; metal avg `0.0354` n `20`; unknown avg `-0.0234` n `784`
- 1h: commodity avg `0.1338` n `12`; crypto_alt avg `0.0766` n `230`; crypto_major avg `-0.0958` n `8`; equity avg `-0.2397` n `103`; fx avg `-0.009` n `6`; index avg `-0.0284` n `25`; metal avg `0.1026` n `20`; unknown avg `-0.057` n `784`
- 4h: commodity avg `0.1352` n `12`; crypto_alt avg `0.4358` n `230`; crypto_major avg `0.2072` n `8`; equity avg `0.7697` n `103`; fx avg `-0.0047` n `6`; index avg `0.1389` n `25`; metal avg `0.1345` n `20`; unknown avg `-0.3369` n `784`
- 24h: commodity avg `-0.0096` n `12`; crypto_alt avg `0.3694` n `230`; crypto_major avg `0.527` n `8`; equity avg `1.8496` n `102`; fx avg `-0.2168` n `6`; index avg `0.0767` n `25`; metal avg `-0.4069` n `20`; unknown avg `0.0459` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
