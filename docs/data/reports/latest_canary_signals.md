# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T12:37:27.786566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.0675` n `230`; crypto_major avg `-0.066` n `8`; equity avg `0.0369` n `100`; fx avg `0.0001` n `6`; index avg `0.0153` n `25`; metal avg `0.0056` n `20`; unknown avg `-0.0093` n `776`
- 1h: commodity avg `0.1879` n `12`; crypto_alt avg `-0.3389` n `230`; crypto_major avg `-0.3354` n `8`; equity avg `-0.0727` n `100`; fx avg `-0.0153` n `6`; index avg `-0.022` n `25`; metal avg `-0.1016` n `20`; unknown avg `0.0199` n `776`
- 4h: commodity avg `0.1935` n `12`; crypto_alt avg `-0.3332` n `230`; crypto_major avg `-0.3999` n `8`; equity avg `-0.4432` n `100`; fx avg `-0.046` n `6`; index avg `-0.069` n `25`; metal avg `-0.089` n `20`; unknown avg `-0.1998` n `775`
- 24h: commodity avg `-0.4481` n `12`; crypto_alt avg `0.1554` n `230`; crypto_major avg `0.7998` n `8`; equity avg `0.7859` n `100`; fx avg `0.0731` n `6`; index avg `0.0802` n `25`; metal avg `0.2718` n `20`; unknown avg `-0.1399` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
