# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T09:07:26.884909+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `12`; crypto_alt avg `0.0929` n `229`; crypto_major avg `0.1996` n `8`; equity avg `-0.0478` n `91`; fx avg `-0.0021` n `6`; index avg `-0.0068` n `25`; metal avg `0.0016` n `20`; unknown avg `5.4115` n `759`
- 1h: commodity avg `0.0696` n `12`; crypto_alt avg `0.0586` n `229`; crypto_major avg `0.2707` n `8`; equity avg `-0.0094` n `91`; fx avg `-0.0113` n `6`; index avg `-0.0009` n `25`; metal avg `0.0173` n `20`; unknown avg `2.7948` n `759`
- 4h: commodity avg `0.3066` n `12`; crypto_alt avg `0.2962` n `229`; crypto_major avg `0.531` n `8`; equity avg `0.6748` n `91`; fx avg `-0.0437` n `6`; index avg `0.1144` n `25`; metal avg `0.1071` n `20`; unknown avg `3.9901` n `743`
- 24h: commodity avg `0.5006` n `12`; crypto_alt avg `0.5102` n `229`; crypto_major avg `-0.0857` n `8`; equity avg `-1.5036` n `90`; fx avg `-0.0746` n `6`; index avg `-0.3572` n `25`; metal avg `-0.3484` n `20`; unknown avg `-0.4709` n `741`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0554`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
