# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T16:22:33.252859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0688` n `12`; crypto_alt avg `-0.0428` n `230`; crypto_major avg `0.1334` n `8`; equity avg `-0.084` n `102`; fx avg `-0.0023` n `6`; index avg `-0.0305` n `25`; metal avg `0.0127` n `20`; unknown avg `0.0368` n `774`
- 1h: commodity avg `0.1481` n `12`; crypto_alt avg `-0.303` n `230`; crypto_major avg `-0.2217` n `8`; equity avg `-0.2769` n `102`; fx avg `-0.002` n `6`; index avg `-0.099` n `25`; metal avg `0.0217` n `20`; unknown avg `-0.3689` n `774`
- 4h: commodity avg `-0.011` n `12`; crypto_alt avg `-1.5995` n `230`; crypto_major avg `-1.2397` n `8`; equity avg `-2.5631` n `102`; fx avg `-0.0552` n `6`; index avg `-0.5498` n `25`; metal avg `0.0416` n `20`; unknown avg `-0.2584` n `774`
- 24h: commodity avg `-0.4623` n `12`; crypto_alt avg `-1.5907` n `230`; crypto_major avg `-0.8283` n `8`; equity avg `-1.9543` n `102`; fx avg `0.0391` n `6`; index avg `-0.51` n `25`; metal avg `0.2813` n `20`; unknown avg `-0.405` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2002`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
