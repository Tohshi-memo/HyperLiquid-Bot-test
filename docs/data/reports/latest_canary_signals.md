# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T14:07:20.993254+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0484` n `12`; crypto_alt avg `-0.3432` n `228`; crypto_major avg `-0.273` n `8`; equity avg `-0.3681` n `67`; fx avg `-0.0074` n `6`; index avg `-0.2135` n `23`; metal avg `-0.2171` n `18`; unknown avg `-0.2806` n `386`
- 1h: commodity avg `0.3965` n `12`; crypto_alt avg `-0.9547` n `228`; crypto_major avg `-0.4389` n `8`; equity avg `-0.2886` n `67`; fx avg `0.0011` n `6`; index avg `0.0732` n `23`; metal avg `-0.4381` n `18`; unknown avg `-0.0843` n `386`
- 4h: commodity avg `-0.4287` n `12`; crypto_alt avg `0.1461` n `228`; crypto_major avg `0.3858` n `8`; equity avg `0.0774` n `67`; fx avg `-0.0372` n `6`; index avg `0.2025` n `23`; metal avg `-0.7748` n `18`; unknown avg `0.519` n `386`
- 24h: commodity avg `-1.3845` n `12`; crypto_alt avg `2.1319` n `228`; crypto_major avg `0.9541` n `8`; equity avg `0.7899` n `67`; fx avg `0.1176` n `6`; index avg `0.8081` n `23`; metal avg `0.3109` n `18`; unknown avg `1.5867` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0448`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0409`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0405`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0402`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.038`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0377`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.034`, n `668`, weak_sample_signal
