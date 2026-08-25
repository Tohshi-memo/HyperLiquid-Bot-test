# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T18:22:30.403267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0079` n `12`; crypto_alt avg `0.3024` n `231`; crypto_major avg `0.2506` n `8`; equity avg `0.1358` n `122`; fx avg `0.0011` n `6`; index avg `0.0052` n `25`; metal avg `0.0023` n `20`; unknown avg `0.1572` n `795`
- 1h: commodity avg `-0.0036` n `12`; crypto_alt avg `0.4986` n `231`; crypto_major avg `0.5858` n `8`; equity avg `0.0347` n `122`; fx avg `0.0022` n `6`; index avg `-0.009` n `25`; metal avg `0.015` n `20`; unknown avg `0.1816` n `795`
- 4h: commodity avg `0.0224` n `12`; crypto_alt avg `0.4668` n `231`; crypto_major avg `0.7238` n `8`; equity avg `0.5448` n `122`; fx avg `-0.0155` n `6`; index avg `0.0202` n `25`; metal avg `0.2141` n `20`; unknown avg `0.1072` n `795`
- 24h: commodity avg `-0.5902` n `12`; crypto_alt avg `-0.3955` n `231`; crypto_major avg `0.9465` n `8`; equity avg `1.3408` n `122`; fx avg `0.0591` n `6`; index avg `0.1192` n `25`; metal avg `-0.0289` n `20`; unknown avg `-0.6255` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
