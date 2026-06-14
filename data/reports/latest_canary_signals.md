# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T10:52:28.333151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0014` n `12`; crypto_alt avg `-0.1811` n `228`; crypto_major avg `-0.1881` n `8`; equity avg `-0.0673` n `74`; fx avg `-0.0068` n `6`; index avg `-0.0045` n `23`; metal avg `-0.0405` n `18`; unknown avg `0.1863` n `645`
- 1h: commodity avg `0.0324` n `12`; crypto_alt avg `-0.1169` n `228`; crypto_major avg `0.0487` n `8`; equity avg `0.1038` n `74`; fx avg `0.0123` n `6`; index avg `0.1001` n `23`; metal avg `-0.0284` n `18`; unknown avg `0.4892` n `645`
- 4h: commodity avg `-0.0639` n `12`; crypto_alt avg `0.1646` n `228`; crypto_major avg `0.3113` n `8`; equity avg `0.3584` n `74`; fx avg `0.0007` n `6`; index avg `0.079` n `23`; metal avg `-0.0148` n `18`; unknown avg `0.6523` n `629`
- 24h: commodity avg `-0.6648` n `12`; crypto_alt avg `0.4014` n `228`; crypto_major avg `1.024` n `8`; equity avg `0.9865` n `74`; fx avg `-0.0194` n `6`; index avg `0.3594` n `23`; metal avg `0.1638` n `18`; unknown avg `-0.536` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
