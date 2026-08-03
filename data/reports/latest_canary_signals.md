# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T20:52:42.267911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0318` n `12`; crypto_alt avg `-0.1086` n `230`; crypto_major avg `-0.2242` n `8`; equity avg `-0.0073` n `103`; fx avg `0.0055` n `6`; index avg `0.0049` n `25`; metal avg `-0.009` n `20`; unknown avg `0.0631` n `784`
- 1h: commodity avg `-0.0309` n `12`; crypto_alt avg `0.0145` n `230`; crypto_major avg `-0.1202` n `8`; equity avg `0.0323` n `103`; fx avg `0.0254` n `6`; index avg `0.0473` n `25`; metal avg `0.0477` n `20`; unknown avg `0.0736` n `784`
- 4h: commodity avg `0.0757` n `12`; crypto_alt avg `0.1495` n `230`; crypto_major avg `0.0048` n `8`; equity avg `0.9081` n `103`; fx avg `0.0204` n `6`; index avg `0.1688` n `25`; metal avg `0.1653` n `20`; unknown avg `-0.137` n `784`
- 24h: commodity avg `-0.1246` n `12`; crypto_alt avg `0.2965` n `230`; crypto_major avg `0.3958` n `8`; equity avg `1.9922` n `103`; fx avg `-0.2589` n `6`; index avg `0.1238` n `25`; metal avg `-0.3771` n `20`; unknown avg `0.0151` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
