# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T20:52:27.676894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0194` n `12`; crypto_alt avg `-0.0536` n `228`; crypto_major avg `-0.0444` n `8`; equity avg `-0.016` n `74`; fx avg `-0.0344` n `6`; index avg `-0.0094` n `23`; metal avg `-0.0167` n `18`; unknown avg `0.0252` n `645`
- 1h: commodity avg `-0.1868` n `12`; crypto_alt avg `0.4156` n `228`; crypto_major avg `0.3779` n `8`; equity avg `0.0686` n `74`; fx avg `-0.0279` n `6`; index avg `-0.0107` n `23`; metal avg `0.0788` n `18`; unknown avg `0.0344` n `645`
- 4h: commodity avg `0.0808` n `12`; crypto_alt avg `0.3995` n `228`; crypto_major avg `0.3957` n `8`; equity avg `0.0527` n `74`; fx avg `-0.0317` n `6`; index avg `-0.0236` n `23`; metal avg `0.0525` n `18`; unknown avg `0.1975` n `645`
- 24h: commodity avg `-0.1044` n `12`; crypto_alt avg `-0.7293` n `228`; crypto_major avg `-0.1845` n `8`; equity avg `0.2817` n `74`; fx avg `-0.0758` n `6`; index avg `0.1056` n `23`; metal avg `-0.0899` n `18`; unknown avg `1.1142` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
