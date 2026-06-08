# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T07:37:25.400984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1314` n `12`; crypto_alt avg `0.2053` n `228`; crypto_major avg `0.0464` n `8`; equity avg `0.1029` n `74`; fx avg `0.0133` n `6`; index avg `0.051` n `23`; metal avg `0.0456` n `18`; unknown avg `0.033` n `517`
- 1h: commodity avg `-0.2402` n `12`; crypto_alt avg `0.2238` n `228`; crypto_major avg `0.3617` n `8`; equity avg `0.6109` n `74`; fx avg `-0.0039` n `6`; index avg `0.2727` n `23`; metal avg `0.3639` n `18`; unknown avg `0.0568` n `517`
- 4h: commodity avg `0.1557` n `12`; crypto_alt avg `0.2547` n `228`; crypto_major avg `0.0014` n `8`; equity avg `-0.3872` n `74`; fx avg `-0.1826` n `6`; index avg `-0.1254` n `23`; metal avg `-0.0176` n `18`; unknown avg `-0.1951` n `507`
- 24h: commodity avg `0.6617` n `12`; crypto_alt avg `0.4482` n `228`; crypto_major avg `1.9357` n `8`; equity avg `0.6513` n `74`; fx avg `-0.293` n `6`; index avg `0.1655` n `23`; metal avg `-0.5333` n `18`; unknown avg `-5.4885` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
