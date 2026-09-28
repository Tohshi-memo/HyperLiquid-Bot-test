# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T23:52:33.279943+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.1334` n `234`; crypto_major avg `0.0116` n `8`; equity avg `-0.0755` n `141`; fx avg `0.0189` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0157` n `20`; unknown avg `0.2423` n `963`
- 1h: commodity avg `-0.036` n `12`; crypto_alt avg `0.729` n `234`; crypto_major avg `0.2107` n `8`; equity avg `-0.0124` n `141`; fx avg `-0.018` n `6`; index avg `-0.0123` n `26`; metal avg `0.0162` n `20`; unknown avg `-0.1916` n `961`
- 4h: commodity avg `0.0959` n `12`; crypto_alt avg `0.9949` n `234`; crypto_major avg `0.1574` n `8`; equity avg `0.0207` n `141`; fx avg `-0.0134` n `6`; index avg `0.0013` n `26`; metal avg `-0.0379` n `20`; unknown avg `-0.2235` n `873`
- 24h: commodity avg `0.0478` n `12`; crypto_alt avg `-3.4502` n `234`; crypto_major avg `-1.9368` n `8`; equity avg `-2.9793` n `141`; fx avg `0.0593` n `6`; index avg `-0.2515` n `26`; metal avg `-0.9567` n `20`; unknown avg `90.6816` n `804`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
