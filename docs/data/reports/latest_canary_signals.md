# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T15:37:16.165132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2374` n `12`; crypto_alt avg `0.2756` n `228`; crypto_major avg `0.0955` n `8`; equity avg `-0.0083` n `67`; fx avg `-0.003` n `6`; index avg `0.0528` n `23`; metal avg `0.1045` n `18`; unknown avg `-0.0583` n `386`
- 1h: commodity avg `-0.3315` n `12`; crypto_alt avg `-0.0759` n `228`; crypto_major avg `-0.1761` n `8`; equity avg `0.021` n `67`; fx avg `0.0246` n `6`; index avg `0.1265` n `23`; metal avg `0.467` n `18`; unknown avg `-0.1546` n `386`
- 4h: commodity avg `-1.0218` n `12`; crypto_alt avg `-0.4538` n `228`; crypto_major avg `-0.2409` n `8`; equity avg `0.0905` n `67`; fx avg `-0.0013` n `6`; index avg `0.4619` n `23`; metal avg `-0.3375` n `18`; unknown avg `0.7202` n `386`
- 24h: commodity avg `-2.2588` n `12`; crypto_alt avg `1.1172` n `228`; crypto_major avg `-0.2655` n `8`; equity avg `0.9896` n `67`; fx avg `0.1553` n `6`; index avg `1.3245` n `23`; metal avg `0.1634` n `18`; unknown avg `-0.4532` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0439`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0426`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.041`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0409`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0396`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0386`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0337`, n `668`, weak_sample_signal
