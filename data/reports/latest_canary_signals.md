# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T22:22:33.685322+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0271` n `13`; crypto_alt avg `0.0721` n `236`; crypto_major avg `0.0788` n `8`; equity avg `-0.0325` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0123` n `26`; metal avg `-0.0039` n `20`; unknown avg `0.2926` n `1191`
- 1h: commodity avg `-0.0568` n `13`; crypto_alt avg `0.028` n `236`; crypto_major avg `0.0843` n `8`; equity avg `-0.2901` n `151`; fx avg `-0.0067` n `6`; index avg `-0.0425` n `26`; metal avg `0.0063` n `20`; unknown avg `1.1499` n `1189`
- 4h: commodity avg `-0.0576` n `13`; crypto_alt avg `0.5507` n `236`; crypto_major avg `0.4849` n `8`; equity avg `-0.545` n `151`; fx avg `0.0095` n `6`; index avg `-0.0722` n `26`; metal avg `0.0564` n `20`; unknown avg `4.1254` n `1107`
- 24h: commodity avg `0.3591` n `13`; crypto_alt avg `-1.5114` n `236`; crypto_major avg `-1.3339` n `8`; equity avg `-4.2038` n `151`; fx avg `0.0238` n `6`; index avg `-0.6744` n `26`; metal avg `-0.0874` n `20`; unknown avg `39.8412` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1632`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1143`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1132`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.077`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0717`, n `666`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.07`, n `666`, weak_sample_signal
