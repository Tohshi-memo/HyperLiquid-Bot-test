# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T23:07:30.355029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.17` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7672` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.757` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6939` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0215` n `12`; crypto_alt avg `0.063` n `228`; crypto_major avg `-0.0856` n `8`; equity avg `-0.0337` n `77`; fx avg `-0.008` n `6`; index avg `-0.0906` n `23`; metal avg `0.0404` n `18`; unknown avg `0.1454` n `687`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `-0.9292` n `228`; crypto_major avg `-0.9834` n `8`; equity avg `-0.2206` n `77`; fx avg `0.0132` n `6`; index avg `-0.0984` n `23`; metal avg `-0.013` n `18`; unknown avg `1.7202` n `687`
- 4h: commodity avg `0.0592` n `12`; crypto_alt avg `-1.7369` n `228`; crypto_major avg `-1.8273` n `8`; equity avg `-0.0601` n `77`; fx avg `0.0325` n `6`; index avg `-0.0703` n `23`; metal avg `-0.1334` n `18`; unknown avg `1.1347` n `679`
- 24h: commodity avg `0.3626` n `12`; crypto_alt avg `1.1094` n `228`; crypto_major avg `2.5606` n `8`; equity avg `1.7036` n `76`; fx avg `-0.0404` n `6`; index avg `0.9315` n `23`; metal avg `0.3435` n `18`; unknown avg `2.1517` n `519`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0459`, n `668`, weak_sample_signal
