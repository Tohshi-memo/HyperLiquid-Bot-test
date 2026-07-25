# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T15:22:28.853935+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `0.1863` n `230`; crypto_major avg `0.1456` n `8`; equity avg `-0.0145` n `100`; fx avg `-0.0048` n `6`; index avg `-0.0077` n `25`; metal avg `0.002` n `20`; unknown avg `0.2503` n `774`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.3062` n `230`; crypto_major avg `0.4835` n `8`; equity avg `0.0424` n `100`; fx avg `0.0037` n `6`; index avg `-0.0072` n `25`; metal avg `0.0195` n `20`; unknown avg `-0.02` n `774`
- 4h: commodity avg `-0.3643` n `12`; crypto_alt avg `0.4758` n `230`; crypto_major avg `0.5649` n `8`; equity avg `0.0208` n `100`; fx avg `-0.002` n `6`; index avg `-0.0082` n `25`; metal avg `0.0249` n `20`; unknown avg `0.0088` n `774`
- 24h: commodity avg `-0.3583` n `12`; crypto_alt avg `0.0672` n `230`; crypto_major avg `0.3913` n `8`; equity avg `-1.0816` n `100`; fx avg `-0.0246` n `6`; index avg `-0.1748` n `25`; metal avg `-0.1871` n `20`; unknown avg `-0.4014` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1642`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1244`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1151`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1085`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
