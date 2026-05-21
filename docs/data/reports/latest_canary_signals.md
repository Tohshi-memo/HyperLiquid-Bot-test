# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T10:07:27.180674+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.14` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.0814` n `228`; crypto_major avg `-0.1033` n `8`; equity avg `-0.0543` n `66`; fx avg `-0.0096` n `6`; index avg `-0.0432` n `23`; metal avg `-0.0689` n `18`; unknown avg `0.0744` n `386`
- 1h: commodity avg `-0.2173` n `12`; crypto_alt avg `-0.4638` n `228`; crypto_major avg `-0.3991` n `8`; equity avg `-0.0627` n `66`; fx avg `0.0324` n `6`; index avg `-0.0637` n `23`; metal avg `-0.0533` n `18`; unknown avg `0.1516` n `386`
- 4h: commodity avg `-0.6068` n `12`; crypto_alt avg `0.2203` n `228`; crypto_major avg `0.2083` n `8`; equity avg `0.0365` n `66`; fx avg `-0.0211` n `6`; index avg `-0.0004` n `23`; metal avg `0.0409` n `18`; unknown avg `0.8424` n `385`
- 24h: commodity avg `-2.3043` n `12`; crypto_alt avg `2.2305` n `228`; crypto_major avg `2.873` n `8`; equity avg `1.5754` n `66`; fx avg `0.1064` n `6`; index avg `1.2709` n `23`; metal avg `0.2633` n `18`; unknown avg `8.0206` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0566`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0502`, n `668`, weak_sample_signal
