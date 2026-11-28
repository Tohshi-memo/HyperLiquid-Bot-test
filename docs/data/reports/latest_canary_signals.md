# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T07:52:28.949044+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `-0.0954` n `239`; crypto_major avg `0.095` n `8`; equity avg `0.0343` n `168`; fx avg `0.0` n `6`; index avg `0.0038` n `27`; metal avg `-0.0106` n `20`; unknown avg `0.5822` n `1269`
- 1h: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.0664` n `239`; crypto_major avg `-0.1109` n `8`; equity avg `0.109` n `168`; fx avg `-0.0038` n `6`; index avg `0.0098` n `27`; metal avg `-0.0016` n `20`; unknown avg `211.8159` n `1257`
- 4h: commodity avg `-0.0124` n `13`; crypto_alt avg `-1.258` n `239`; crypto_major avg `-0.5169` n `8`; equity avg `-0.057` n `168`; fx avg `-0.0124` n `6`; index avg `-0.0311` n `27`; metal avg `-0.0048` n `20`; unknown avg `1.4301` n `1209`
- 24h: commodity avg `-0.793` n `13`; crypto_alt avg `-2.8859` n `239`; crypto_major avg `-2.5591` n `8`; equity avg `0.2937` n `168`; fx avg `-0.1037` n `6`; index avg `0.0729` n `27`; metal avg `-0.2943` n `20`; unknown avg `215.3837` n `969`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1427`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1426`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
