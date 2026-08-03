# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T19:37:36.621662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `12`; crypto_alt avg `-0.0213` n `230`; crypto_major avg `-0.0064` n `8`; equity avg `-0.0112` n `103`; fx avg `0.0025` n `6`; index avg `0.0051` n `25`; metal avg `0.0151` n `20`; unknown avg `-0.1282` n `784`
- 1h: commodity avg `-0.0095` n `12`; crypto_alt avg `-0.0455` n `230`; crypto_major avg `-0.0142` n `8`; equity avg `0.1583` n `103`; fx avg `0.0065` n `6`; index avg `0.0337` n `25`; metal avg `0.1107` n `20`; unknown avg `-0.1013` n `784`
- 4h: commodity avg `0.1092` n `12`; crypto_alt avg `0.3795` n `230`; crypto_major avg `0.1175` n `8`; equity avg `1.1507` n `103`; fx avg `0.0057` n `6`; index avg `0.1702` n `25`; metal avg `0.1851` n `20`; unknown avg `-0.1795` n `784`
- 24h: commodity avg `0.0014` n `12`; crypto_alt avg `0.4102` n `230`; crypto_major avg `0.5696` n `8`; equity avg `1.9202` n `103`; fx avg `-0.2594` n `6`; index avg `0.0762` n `25`; metal avg `-0.3827` n `20`; unknown avg `0.001` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
